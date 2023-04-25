# Built-in library imports
# import json

# discord.py imports
import discord
from discord import app_commands
from discord.ext import commands


class BotProperties(commands.Cog):
    """
    Events/commands related to monitoring/altering the bot's properties.
    """

    def __init__(self, bot):
        self.bot = bot

    ##### EVENTS #############################################################

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

    @app_commands.command(name='ping', description="Displays the bot's latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Latency {round(self.bot.latency * 1000)} ms")

    # @commands.command()
    # @commands.is_owner()
    # async def sync(self, ctx):
    #     # TODO delete
    #     await self.bot.tree.sync()
    #     synced_cmds = await self.bot.tree.sync()   # https://stackoverflow.com/questions/74413367/how-to-sync-slash-command-globally-discord-py
    #     await ctx.send(f"Synced the following commands: {f'{cmd}, ' for cmd in synced_cmds}")

    # @app_commands.command(name='sync', description="Syncs slash commands with all guilds")
    # @commands.is_owner()
    # async def sync(self):
    #     """Syncs slash commands with all guilds."""
    #     synced_cmds = await self.bot.tree.sync()   # https://stackoverflow.com/questions/74413367/how-to-sync-slash-command-globally-discord-py
    #     ctx.send(f"Synced the following commands: {f'{cmd}, ' for cmd in synced_cmds}")

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


async def setup(bot):
    await bot.add_cog(BotProperties(bot))
