from discord.ext import commands
from sql.poll import SqlClass


class Poll(commands.Cog, name='poll'):
    """
    Poll commands
    """
    def __init__(self, client):
        self.client = client
        self.sql = SqlClass()

    @commands.command()
    async def test(self, ctx):
        await ctx.send('ping')


def setup(client):
    client.add_cog(Poll(client))
