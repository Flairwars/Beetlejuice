from discord.ext import commands


class Count(commands.Cog, name='count'):
    """
    Counts different subreddits
    """
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test4(self, ctx):
        await ctx.send('ping')


def setup(client):
    client.add_cog(Count(client))
