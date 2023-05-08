# standard imports
import io

# discord.py imports
import discord
from discord import app_commands
from discord.ext import commands

# external packages
import aiohttp


class UserInfo(commands.Cog):
    """Commands related to retrieving user info."""

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='pfp', description="Sends the user's profile picture as a jpg.")
    async def pfp(self, interaction: discord.Interaction, member: discord.Member):
        "Sends the user's profile picture as a jpg."
        async with aiohttp.ClientSession() as session:
            async with session.get(member.avatar.url) as response:
                if response.status != 200:
                    return await interaction.response.send_message("Could not download file...")
                data = io.BytesIO(await response.read())
                await interaction.response.send_message(
                    file=discord.File(data, f'{member.name}_avatar.jpg')
                )

    @app_commands.command(name='joindate', description="Sends the date the member first joined this server (UTC format).")
    async def joindate(self, interaction: discord.Interaction, member: discord.Member):
        """Sends the date the member first joined this server (UTC format)."""
        await interaction.response.send_message(member.joined_at)


async def setup(bot):
    await bot.add_cog(UserInfo(bot))
