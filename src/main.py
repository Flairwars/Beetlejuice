from discord.ext import commands
from decouple import config
from discord import Intents
import os
from os import path
import sys

#generate path of colorapp
colorapp_path = path.abspath("colorapp")

#add colorapp to include path
if not colorapp_path in sys.path:
	sys.path.append(colorapp_path)

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
