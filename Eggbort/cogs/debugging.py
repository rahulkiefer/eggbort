from discord.ext import commands


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

        self.bot.load_extension('cogs.{}'.format(extension))
        print('{} was loaded'.format(extension))

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        """Manually unloads a specified cog"""

        self.bot.unload_extension('cogs.{}'.format(extension))
        print('{} was unloaded'.format(extension))

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        """Manually reloads a specified cog"""

        self.bot.unload_extension('cogs.{}'.format(extension))
        self.bot.load_extension('cogs.{}'.format(extension))
        print('{} was reloaded'.format(extension))


def setup(bot):
    bot.add_cog(Debugging(bot))
