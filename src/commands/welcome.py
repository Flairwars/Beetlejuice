from discord.ext import commands
import requests


class Welcome(commands.Cog, name='Welcome'):
    """
    Checks for new users
    """
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Checks A User's ID when they join to give infomation
        """
        fwuserid = member.id
        fw_request_userid = requests.get(f'https://api.flairwars.com/users?DiscordMemberID={fwuserid}')


        if fw_request_userid >0:
            embed = discord.Embed(title=f"Reddit USername varible", color=color, description=description,)
            add field useraccount age discord, reddit account age

        else:
            reddit_auth = f'https://www.reddit.com/api/v1/authorize?client_id{process.env.REDDIT_CLIENTID}&response_type=code&state=${state}&redirect_uri=${redirect_uri}&scope=identity'
            await ctx.send(f'Please sign into Reddit! {reddit_auth}')

            fwuseridnew = member.id
            fw_add_user = requests.post(f'https://api.flairwars.com/users', headers={'Authorization': f'Basic {secret}'}, data={f
                "DiscordMemberID": "{fwuseridnew}",
                "FlairwarsColor": "string",
                "RedditUsername": "string"})



       def  if user color = yellow:
            await ctx.send("Welcome to the Yellow Server, @user! EFHJhgwjehjgkefwghjefwhjgewfjhghgefwhgjsdhshsdhgsdfhgsdfhgsdfhgdhgsdfghjfdsghjsdfghjdsfhsdd"
                           "/n Check out #get-roles to get some sweet roles to reveal more channels and don't forget to join the Yellow server:"
                           "/n User Guides"
                           "/n@A group of people")

       def if user color /= yellow:
            await ctx.send(
                "Welcome to the Yellow Server, @user! EFHJhgwjehjgkefwghjefwhjgewfjhghgefwhgjsdhshsdhgsdfhgsdfhgsdfhgdhgsdfghjfdsghjsdfghjdsfhsdd"
                "/n Check out #get-roles to get some sweet roles to reveal more channels and don't forget to join the Yellow server:"
                "/n User Guides"
                "/n@A group of people")


    @commands.command(name='reauth')
    async def reauth(self, ctx):
        """
        Rechecks for new infomation in FW API
        """

        await ctx.send("test")


    @commands.command(name='welcome')
    async def welcome(self, ctx):
        """
        Welcomes a new user by adding color roles and pings with infomation
        """
        call the right function
        await ctx.send("User Welcomed")

def setup(client):
    client.add_cog(Welcome(client))
