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
    'cogs.help',
    'cogs.poll',
    'cogs.user_info',
)

# TODO re-implement with external DB to store prefixes
# def retrieve_prefix(bot, message):
#     """Returns server prefix for current server on bot startup"""

#     with open(file_paths.SERVER_PREFIXES) as f:
#         server_prefixes = json.load(f)

#     guild_id = str(message.guild.id)

#     if server_prefixes[guild_id] is None:
#         return ('egg!', server_prefixes[guild_id])


class Eggbort(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='e.',
            owner_id='220377491926286337'  #  my Discord user ID
        )

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as _e:
                print(f'Failed to load extension {extension}.')

    async def on_command_error(self, ctx, error):
        """
        Alerts the user if a nonexistent command is used.

        The alert message disappears after five seconds.
        """

        if isinstance(error, commands.CommandNotFound):
            message = await ctx.send('Invalid command')
            await message.delete(delay=5)

    def run(self):
        super().run(os.environ['EGGBORT_TOKEN'])


bot = Eggbort()
bot.run()
