from discord.ext import commands


class Role(commands.Cog, name='role'):
    """
    Persistent roles
    """
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test2(self, ctx):
        await ctx.send('ping')


def setup(client):
    client.add_cog(Role(client))
