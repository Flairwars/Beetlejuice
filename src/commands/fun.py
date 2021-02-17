from discord.ext import commands
import random

class Fun(commands.Cog, name='Fun'):
    """
    F is for friends and uh U is for I forgot and N is for now? Idk this song
    """
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['hug'])
    async def hug(self, ctx, target: discord.Member = None):

        if target is None:
            await ctx.send(f"*hugs back*")

        elif target == ctx.author:
            file = str(5) + '.gif'
            await ctx.send(file=discord.File('src/data/hugs/' + file))
            return

        else:
            file = str(random.randint(1, 26)) + '.gif'
            await ctx.send(file=discord.File('src/data/hugs/' + file))
            return
        await ctx.send('ping')


def setup(client):
    client.add_cog(Fun(client))
