import discord
import git
from discord.ext import commands


class AdminCog(commands.Cog):
#
    """
    Reloads Cogs - Bot Admin Only
    """

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='game')
    @commands.is_owner()
    async def gamestatus(self, ctx, game):
        game = discord.Game(game)
        await self.bot.change_presence(status=discord.Status.online, activity=game)
        embedMsg = discord.Embed(color=0xFCF4A3, title=":sunny::sunflower: Status Changed :sunflower::sunny:")
        await ctx.send(embed=embedMsg)



    @commands.command(name='gitpull')
    @commands.is_owner()
    async def git_pull(self, ctx):
        git_dir = "./"
        try:
            g = git.cmd.Git(git_dir)
            g.pull()
            embed = discord.Embed(title=":white_check_mark: Successfully pulled from repository", color=0x00df00)
            await ctx.channel.send(embed=embed)
        except Exception as e:
            errno, strerror = e.args
            embed = discord.Embed(title="Command Error!",
                                    description=f"Git Pull Error: {errno} - {strerror}",
                                    color=0xff0007)
            await ctx.channel.send(embed=embed)
        else:
            await ctx.send("You don't have access to this command! Ask Pepper about it if you need help!")


def setup(bot):
    bot.add_cog(AdminCog(bot))