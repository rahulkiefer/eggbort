"""standard imports"""
import logging

# discord.py imports
from discord.ext import commands

logging.basicConfig(level=logging.DEBUG)


class Debugging(commands.Cog):
    """Commands related to testing the bot after changes to the code have been
    made.

    This class should be unnecessary after the bot is hosted on the cloud.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        """Manually loads a specified cog"""

        await self.bot.load_extension(f'cogs.{extension}')
        logging.debug('%s was loaded', extension)

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        """Manually unloads a specified cog"""

        await self.bot.unload_extension(f'cogs.{extension}')
        logging.debug('%s was unloaded', extension)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        """Manually reloads a specified cog"""

        await self.bot.unload_extension(f'cogs.{extension}')
        await self.bot.load_extension(f'cogs.{extension}')
        logging.debug('%s was reloaded', extension)

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        """Syncs slash commands with all guilds"""

        synced_cmds = await self.bot.tree.sync()
        await ctx.send(f"Synced {len(synced_cmds)} commands")


async def setup(bot: commands.Bot) -> None:
    """Adds the Debugging cog"""
    await bot.add_cog(Debugging(bot))
