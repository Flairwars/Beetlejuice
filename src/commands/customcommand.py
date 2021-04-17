import traceback
from discord.ext import commands
from sql.customcommand import SqlClass

sql = SqlClass()


def is_private_command():
    async def predicate(ctx):
        guild_id = sql.get_command_guild(ctx.command.name)
        if guild_id:
            return ctx.guild.id == sql.get_command_guild(ctx.command.name)[0][0]
        return False

    return commands.check(predicate)


def main(client, command_name, response):
    class commandTemplate(commands.Cog, name='Custom commands'):
        def __init__(self, client, response, description=""):
            self.client = client
            self.response = response
            self.description = description

        @commands.command(name=command_name)
        @is_private_command()
        async def custom_command(self, ctx):
            f"""
            {self.description}
            """
            await ctx.send(self.response)

        @custom_command.error
        async def _custom_command(self, ctx: object, error: object):
            if not isinstance(error, commands.errors.CheckFailure):
                traceback.print_exc()

    client.add_cog(commandTemplate(client, response))


class customCommand(commands.Cog, name='Custom commands'):
    """
    Custom commands
    """
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ac(self, ctx, command_name, *, response):
        sql.add_command(ctx.guild.id, command_name)
        main(self.client, command_name, response)
        await ctx.send("work")

    @commands.command()
    async def uc(self, ctx, command_name):
        sql.remove_command(ctx.guild.id, command_name)
        self.client.remove_command(command_name)
        await ctx.send("work")


def setup(client):
    client.add_cog(customCommand(client))
