# Built-in library imports
import json

# discord.py imports
from discord import Activity, ActivityType, Status
from discord.ext import commands


class BotProperties(commands.Cog):
    """
    Events/commands related to monitoring/altering the bot's properties.
    """

    def __init__(self, bot):
        self.bot = bot

    ##### EVENTS #############################################################

    @commands.Cog.listener()
    async def on_ready(self):
        """Sets the bot's status and activity upon booting up"""

        await self.bot.change_presence(
            status=Status.online,
            activity=Activity(
                type=ActivityType.playing,
                name='e.help'
            )
        )
        print('Bot is ready.')  # for debugging purposes

    # TODO re-implement with external DB to store prefixes
    # @commands.Cog.listener()
    # async def on_guild_join(self, guild):
    #     """Adds the 'e.' server prefix upon joining a server."""

    #     with open(file_paths.SERVER_PREFIXES, 'r') as f:
    #         server_prefixes = json.load(f)

    #     server_prefixes[str(guild.id)] = 'e.'  # adds the default bot prefix

    #     with open(file_paths.SERVER_PREFIXES, 'w') as f:
    #         json.dump(server_prefixes, f, indent=4)

    # @commands.Cog.listener()
    # async def on_guild_remove(self, guild):
    #     """Removes current server prefix upon leaving a server."""

    #     with open(file_paths.SERVER_PREFIXES, 'r') as f:
    #         server_prefixes = json.load(f)

    #     del server_prefixes[str(guild.id)]

    #     with open(file_paths.SERVER_PREFIXES, 'w') as f:
    #         json.dump(server_prefixes, f, indent=4)

    ##### COMMANDS ###########################################################

    @commands.command()
    async def ping(self, ctx):
        """Displays the bot's latency"""
        await ctx.send('Latency: {} ms'.format(round(self.bot.latency * 1000)))

    # TODO re-implement with external DB to store prefixes
    # @commands.command()
    # @commands.has_permissions(administrator=True)
    # async def serverprefix(self, ctx, *args):
    #     """
    #     Shows (changes) the server prefix (w/ argument)

    #     If the call has an argument, changes the prefix to the argument.
    #     """

    #     with open(file_paths.SERVER_PREFIXES, 'r') as f:
    #         server_prefix = json.load(f)

    #     # if an argument for serverprefix has been given, set it as the new
    #     # prefix
    #     if len(args) > 0:
    #         new_prefix = ' '.join(args)
    #         server_prefix[str(ctx.guild.id)] = new_prefix

    #         with open(file_paths.SERVER_PREFIXES, 'w') as f:
    #             json.dump(server_prefix, f, indent=4)

    #         await ctx.send(
    #             'Server prefix has been updated to: {}'.format(new_prefix)
    #         )

    #     # otherwise just list the current server prefix
    #     else:
    #         await ctx.send(
    #             'Current server prefix is: {}'.format(
    #                 server_prefix[str(ctx.guild.id)]
    #             )
    #         )


def setup(bot):
    bot.add_cog(BotProperties(bot))
