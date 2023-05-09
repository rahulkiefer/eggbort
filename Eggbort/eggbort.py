# standard imports
import logging
import os

# discord.py imports
import discord
from discord import Activity, ActivityType, Status
from discord.ext import commands

# external packges
import wavelink

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
logging.getLogger('discord.http').setLevel(logging.DEBUG)


class Eggbort(commands.Bot):
    """Contains setup needed for bot to successfully start and load commands"""

    def __init__(self):
        super().__init__(
            command_prefix='e.',
            intents=discord.Intents().all()
        )

        self.cog_list = (
            'cogs.bot_properties',
            'cogs.chat_management',
            'cogs.debugging',
            'cogs.fun',
            'cogs.help',
            'cogs.music',
            'cogs.poll',
            'cogs.user_info',
        )

    async def on_ready(self) -> None:
        """Sets the bot's status and activity upon booting up."""

        await self.change_presence(
            status=Status.online,
            activity=Activity(
                type=ActivityType.playing,
                name='/help'
            )
        )
        logging.info('Bot is ready.')  # for debugging purposes

    async def setup_hook(self) -> None:
        """Performs asynchronous setup after the bot is logged in but before it
        has connected to the Websocket.
        """

        # Wavelink
        node: wavelink.Node = wavelink.Node(
            uri='http://lavalink:2333', password='youshallnotpass')
        await wavelink.NodePool.connect(client=self, nodes=[node])

        # cogs
        for ext in self.cog_list:
            try:
                await self.load_extension(ext)
                logging.info("Loaded %s", ext)
            except Exception as _e:
                logging.info("Failed to load extension: %s", ext)

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
        super().run(os.environ['EGGBORT_TOKEN'], log_handler=None)
