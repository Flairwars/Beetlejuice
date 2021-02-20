from discord.ext import commands
from sql.battle import SqlClass

class Battle(commands.Cog, name='Battles and Season Wins'):
    """
    Gives Infomation on Flairwars Battles and Seasons
    """
    def __init__(self, client):
        self.client = client
        self.sql = SqlClass()

    @commands.command()
    async def addcolor(self, ctx, color):
        self.sql.add_color(color)
        await ctx.send('ping')


def setup(client):
    client.add_cog(Battle(client))
