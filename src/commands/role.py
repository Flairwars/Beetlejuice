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

    def update_roles(self, guild):
        """
        Updates Roles in the database
        :param guild:
        :return:
        """
        guild_roles = guild.roles
        guild_id = guild.id

        db_roles = self.sql.get_roles(guild_id)
        db_roles = [db_role[0] for db_role in db_roles]  # Removes tuples from list

        lst = []
        for role in guild_roles:
            role_id = role.id
            role_name = role.name

            if role_id not in db_roles and role_name != "@everyone":
                lst.append(role_id)

        self.sql.add_roles(guild_id, lst)

        lst = []
        for db_role in db_roles:
            if not any(guild_role.id == db_role for guild_role in guild_roles):
                lst.append(db_role)

        self.sql.remove_roles(guild_id, lst)

    def update_guild(self, guild): pass

    @commands.command(aliases=['clearroles','purgeroles'])
    @commands.has_permissions(administrator=True)
    async def removeroles(self, ctx, member: discord.Member = None):
        """Removes a users roles
        :param ctx:
        :param member: The users whos roles are getting removed
        :return: Removes the users role from the database
        """
        guild_id = ctx.guild.id
        if member is None:
            username = ctx.author.name
            user_id = ctx.author.id
        else:
            username = member.name
            user_id = member.id

        message = await ctx.send(f"`purging {username}'s roles from datatables...`")
        self.sql.remove_user_roles(user_id, guild_id)
        await message.edit(content=f"`purged {username}'s roles from datatables!`")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addroles(self, ctx, member: discord.Member):
        """
        Adds user roles to server
        :param ctx:
        :param member: The users whos roles are getting added
        :return: Adds the users roles and removes their roles from the database
        """
        guild = ctx.guild
        username = member.name
        user_id = member.id

        self.update_roles(guild)


        memberId = str(member.id)
        memberGuildId = str(member.guild.id)
        memberRoles = sql.get_user_role(memberId, memberGuildId)

        if len(memberRoles) < 1:
            await ctx.send(f'`{member.name} has no roles in my datatable`')
            return


def setup(client):
    client.add_cog(Role(client))
