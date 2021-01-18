from discord.errors import DiscordException
from discord.ext import commands
from discord.utils import get
import discord
from sql.role import SqlClass # BITCH STOP COMPLAING YOU LITEREALYL WORK. DUMB ASS PROGRAMM


class Role(commands.Cog, name='role'):
    """
    Persistent roles
    """
    def __init__(self, client):
        self.client = client
        self.sql = SqlClass()

    @commands.command(aliases=['removeroles','clearroles','purgeroles'])
    async def remove_roles(self, ctx, member: discord.Member):
        """Removes a users roles
        :param member:
        :param ctx:
        :return:
        """
        message = await ctx.send(f"`purging {ctx.author.name}'s roles from datatables...`")
        self.sql.remove_user_roles(ctx.author.id, ctx.guild.id)
        await message.edit(content=f"`purged {ctx.author.name}'s roles from datatables!`")




def setup(client):
    client.add_cog(Role(client))
