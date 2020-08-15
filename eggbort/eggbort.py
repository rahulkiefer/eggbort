# Built-in library imports
import asyncio
import json
import os

# discord.py imports
import discord
from discord.ext import commands

# My file imports
import file_paths

initial_extensions = (
    'cogs.bot_properties',
    'cogs.chat_management',
    'cogs.debugging',
    'cogs.events',
    'cogs.help',
    'cogs.music',
)


def retrieve_prefix(bot, message):
    """Returns server prefix for current server on bot startup"""

    with open(file_paths.SERVER_PREFIXES) as f:
        server_prefixes = json.load(f)

    return ('egg!', server_prefixes[str(message.guild.id)])


class Eggbort(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=retrieve_prefix)

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as _e:
                print(f'Failed to load extension {extension}.')

    def run(self):
        super().run(
            os.environ('EGGBORT_TOKEN'),
            reconnect=True,
        )


bot = Eggbort()
bot.run()

# bot.remove_command('help')  # removes the default help command
# TODO implement new help command and uncomment line above
