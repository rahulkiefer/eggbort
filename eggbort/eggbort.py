# Built-in library imports
import os
import asyncio
import json

# Discord library imports
import discord
from discord.ext import commands
import eggbort_token

# My file imports
import file_paths

# Note: egg! is now the default (and permanent) prefix
# whenever a serverprefix is added/changed, egg! is still be available


def retrieve_prefix(bot, message):
  """Returns server prefix for current server on bot startup"""

  with open(file_paths.SERVER_PREFIXES) as f:
    server_prefixes = json.load(f)

  return ('egg!', server_prefixes[str(message.guild.id)])


bot = commands.Bot(command_prefix=retrieve_prefix)


##### EVENTS ###################################################################

@bot.event
async def on_command_error(ctx, error):
  """
  Alerts the user if a nonexistent command is used.
  
  The alert message disappears after one second.
  """

  if isinstance(error, commands.CommandNotFound):
    message = await ctx.send('Invalid command')
    await message.delete(delay=1)


# Loads all extensions (Cogs)
for filename in os.listdir('eggbort/cogs'):
  if filename.endswith('.py'):
    bot.load_extension('cogs.{}'.format(filename[:-3]))  # [:-3] gets rid of .py


bot.run(eggbort_token.TOKEN)

# TODO
# Voice ideas:
# "Destroooooy him"
# "Jock shock"
# The Rats song
# The Rats birthday song

# move a user into a channel and play loud noise
# music capability in general
