import discord
from discord import app_commands
from discord.ext import commands


class ChatManagement(commands.Cog):
    """
    Commands related to managing chat.
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='clear', description="Deletes the specified number of messages above.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        """
        Deletes the specified number of messages above.

        By default, with no number given, the clear command itself and the
        message above it will be deleted.
        """
        if amount < 1:
            await interaction.response.send_message(
                content="Cannot clear less than 1 message.",
                ephemeral=True
            )
            await interaction.message.delete()
        else:
            await interaction.response.defer()
            await interaction.channel.purge(limit=amount + 1)


async def setup(bot):
    await bot.add_cog(ChatManagement(bot))
