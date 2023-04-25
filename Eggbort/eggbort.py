# Built-in library imports
import asyncio
import logging
import os

# discord.py imports
import discord
import wavelink
from discord import Activity, ActivityType, Status
from discord.ext import commands

logging.basicConfig(level=logging.DEBUG)

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
            intents=discord.Intents().all(),
            owner_id='220377491926286337'  #  my Discord user ID
        )

        self.cog_list = (
            'cogs.bot_properties',
            'cogs.chat_management',    # need to migrate to slash cmds
            'cogs.debugging',   # need to migrate to slash cmds
            'cogs.help',  # need to migrate to slash cmds
            'cogs.new_music',   # need to migrate to slash cmds
            'cogs.poll',  # need to migrate to slash cmds
            'cogs.user_info', # need to migrate to slash cmds
        )
    
    async def on_ready(self) -> None:
        """Sets the bot's status and activity upon booting up."""

        await self.change_presence(
            status=Status.online,
            activity=Activity(
                type=ActivityType.playing,
                name='e.help'
            )
        )
        logging.debug('Bot is ready.')  # for debugging purposes

    async def setup_hook(self) -> None:
        """Performs asynchronous setup after the bot is logged in but before it has connected to the Websocket."""

        # cogs
        for ext in self.cog_list:
            try:
                await self.load_extension(ext)
                logging.debug(f"Loaded {ext}")
            except Exception as _e:
                logging.debug(f'Failed to load extension {ext}.')

        # Wavelink
        node: wavelink.Node = wavelink.Node(uri='http://lavalink:2333', password='youshallnotpass')
        await wavelink.NodePool.connect(client=self, nodes=[node])

    # async def on_command_error(self, ctx, error):
    #     '''General error-handling for commands.'''

    #     if isinstance(error, commands.CommandNotFound):
    #         await ctx.send('Invalid command')

    #     elif isinstance(error, commands.MissingPermissions):
    #         perms = ', '.join(error.missing_perms)
    #         await ctx.send(
    #             f'You are missing the following permission(s) to invoke this command: {perms}'
    #         )

    #     elif isinstance(error, commands.BotMissingPermissions):
    #         perms = ', '.join(error.missing_perms)
    #         await ctx.send(
    #             f'I need the following permission(s) to run this command: {perms}'
    #         )

    def run(self) -> None:
        super().run(os.environ['EGGBORT_TOKEN'])
