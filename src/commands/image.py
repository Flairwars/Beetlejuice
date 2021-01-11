from discord.ext import commands
from PIL import Image
from functools import partial
import discord
import aiohttp
import re
import io


class ImageEditing(commands.Cog, name='image'):
    """
    Image editing
    """

    def __init__(self, client):
        self.client = client
        self.msgLimit = 25
        self.reg = re.compile(r'https?:/.*\.(png|jpg|jpeg|gif|jfif|bmp)')

    @staticmethod
    def imageProcessing(img, color, strength):
        """
        recolors
        """
        for i in range(0, img.size[0]):  # process all pixels
            for j in range(0, img.size[1]):
                pixel_data = img.getpixel((i, j))
                new_color = tuple(abs(pixel_data[n] + round(color[n] * strength)) for n in range(4))
                img.putpixel((i, j), new_color)

        return img

    @commands.command(aliases=['rc', 'recolour'])
    async def recolor(self, ctx: object, color: str = 'yellow', strength: float = 100):
        """
        Recolors above image
        :param color:
        :param strength:
        :return Recolored image:
        """
        color = color.lower()
        # Strength and color definitions
        strength /= 100

        addition_colors = {
            'red': (255, -255, -255, 0),
            'orange': (255, 127, 0, 0),
            'yellow': (255, 255, -255, 0),
            'green': (-255, 255, -255, 0),
            'blue': (-255, -255, 255, 0),
            'purple': (127, -255, 127, 0),
            'r': 'red',
            'o': 'orange',
            'y': 'yellow',
            'g': 'green',
            'b': 'blue',
            'p': 'purple'
        }
        if len(color) == 1:
            color = addition_colors[color]

        if color not in addition_colors:
            raise discord.errors.DiscordException
            # What to do when no attachment is sent with the file: Search prev. messages for a file, also for links.

        bot_msg = await ctx.send('`Editing images`')
        async with ctx.typing():
            if ctx.message.attachments:
                data = await ctx.message.attachments[0].read()
            else:
                async for msg in ctx.channel.history(limit=self.msgLimit):
                    # loop through x messages
                    if msg.attachments:
                        file_url = msg.attachments[0].url
                    else:
                        file_url = ''

                    message_url = self.reg.search(msg.content)
                    if message_url:
                        message_url = message_url.group(0)

                    # print(file_url, message_url)
                    if self.reg.match(file_url) or message_url:  # self.reg to check for images in links
                        url = file_url if file_url else message_url
                        # found attachment with image file format
                        async with aiohttp.ClientSession() as session:
                            async with session.get(url) as response:
                                data = await response.read()
                        break
                else:
                    await bot_msg.edit(content='`No image found`')
                    return

            await bot_msg.edit(content='`Image found!`')
            img = Image.open(io.BytesIO(data))
            img = img.convert('RGBA')  # In case image (e.g. JPG) is in 'RGB' or else mode.

            fn = partial(self.imageProcessing, img, addition_colors[color], strength)
            img = await self.client.loop.run_in_executor(None, fn)

            # Send image to discord without saving to file
            img_bytes_arr = io.BytesIO()
            img.save(img_bytes_arr, format='PNG')
            img_bytes_arr.seek(0)
            f = discord.File(img_bytes_arr, 'recolour.png')

        await ctx.send(f'`{color}@{int(strength * 100)}%`', file=f)
        await bot_msg.delete()

    @recolor.error
    async def _recolor(self, ctx: object, error: object):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('`ERROR: invalid args <color> <percentage>`')
        elif isinstance(error, discord.errors.DiscordException):
            await ctx.send('`ERROR: invalid color`')
        else:
            await ctx.send('`ERROR: something went wrong`')

    @commands.command(alieses=['bee'])
    async def beeify(self, ctx):
        await ctx.send('ping')


def setup(client):
    client.add_cog(ImageEditing(client))
