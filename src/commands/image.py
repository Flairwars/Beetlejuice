from discord.ext import commands


class Image(commands.Cog, name='image'):
    """
    Image editing
    """
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test3(self, ctx):
        await ctx.send('ping')


def setup(client):
    client.add_cog(Image(client))
