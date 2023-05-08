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

    ##### COMMANDS ###########################################################

    @app_commands.command(name='ping', description="Displays the bot's latency")
    async def ping(self, interaction: discord.Interaction):
        """Displays the bot's latency"""
        await interaction.response.send_message(f"Latency {round(self.bot.latency * 1000)} ms")


async def setup(bot):
    await bot.add_cog(BotProperties(bot))
