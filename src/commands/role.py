from discord.ext import commands
from sql_funct.role import SqlClass # BITCH STOP COMPLAING YOU LITEREALYL WORK. DUMB ASS PROGRAMM


class Role(commands.Cog, name='role'):
    """
    Persistent roles
    """
    def __init__(self, client):
        self.client = client
        sql = SqlClass()

    @commands.command()
    async def test2(self, ctx):
        await ctx.send('ping')


def setup(client):
    client.add_cog(Role(client))
