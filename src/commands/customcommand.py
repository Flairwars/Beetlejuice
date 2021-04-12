from discord.ext import commands


def main(client, command_name, response):
    class commandTemplate(commands.Cog, name='Custom commands'):
        def __init__(self, client, response):
            self.client = client
            self.response = response

        @commands.command(name=command_name)
        async def custom_command(self, ctx):
            await ctx.send(self.response)

    client.add_cog(commandTemplate(client, response))


class customCommand(commands.Cog, name='Custom commands'):
    """
    Custom commands
    """
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ac(self, ctx, command_name, *, response):
        main(self.client, command_name, response)
        await ctx.send("work")


def setup(client):
    client.add_cog(customCommand(client))
