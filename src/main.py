from discord.ext import commands
from decouple import config
from discord import Intents
import os

#setting up cppinclude
#included here for library structure reasons
import cppimport.import_hook
import colorapp.cpp

# add discord bot perms
intents = Intents.default()
intents.presences = True
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)

# loads all cogs
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')


# prints when bot has started up
@client.event
async def on_ready():
    print('bot done')


client.run(config('TOKEN'))
