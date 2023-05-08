import discord
from discord import app_commands
from discord.ext import commands


class Poll(commands.Cog):
    """
    Commands that relate to creating polls.

    Any commands that interact with users' reactions on messages (e.g. raffle
    winner selection, etc.).
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='poll', description="Creates a poll using reactions.")
    async def poll(self, interaction: discord.Interaction, question: str):
        """Creates a poll using reactions."""
        embed = discord.Embed(
            title="Poll",
            description=question,
            color=discord.Color.from_rgb(255, 215, 154)
        )
        embed.set_footer(
            text=f"Vote with the reactions below."
        )

        await interaction.response.send_message(embed=embed)

        sent_msg = await interaction.original_response()
        await sent_msg.add_reaction('👍')
        await sent_msg.add_reaction('👎')
        await sent_msg.add_reaction('🤷')


async def setup(bot):
    await bot.add_cog(Poll(bot))
