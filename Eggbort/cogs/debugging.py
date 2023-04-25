import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.DEBUG)

class Debugging(commands.Cog):
    """Commands related to testing the bot after changes to the code have been
    made.

    This class should be unnecessary after the bot is hosted on the cloud.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # @commands.is_owner()
    async def load(self, ctx, extension):
        """Manually loads a specified cog"""

        await self.bot.load_extension('cogs.{}'.format(extension))
        logging.debug('{} was loaded'.format(extension))

    @commands.command()
    # @commands.is_owner()
    async def unload(self, ctx, extension):
        """Manually unloads a specified cog"""

        await self.bot.unload_extension('cogs.{}'.format(extension))
        logging.debug('{} was unloaded'.format(extension))

    @commands.command()
    # @commands.is_owner()
    async def reload(self, ctx, extension):
        """Manually reloads a specified cog"""

        await self.bot.unload_extension('cogs.{}'.format(extension))
        await self.bot.load_extension('cogs.{}'.format(extension))
        logging.debug('{} was reloaded'.format(extension))

    @commands.command()
    async def sync(self, ctx):
        synced_cmds = await self.bot.tree.sync()   # https://stackoverflow.com/questions/74413367/how-to-sync-slash-command-globally-discord-py
        await ctx.send(f"Synced {len(synced_cmds)} commands")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Debugging(bot))
