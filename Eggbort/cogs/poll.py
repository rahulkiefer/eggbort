from discord.ext import commands


class Poll(commands.Cog):
    """
    Commands that relate to creating polls.

    Any commands that interact with users' reactions on messages (e.g. raffle
    winner selection, etc.).
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx):
        """Creates a poll using reactions on the creator's message"""
        message = ctx.message
        await message.add_reaction('👍')
        await message.add_reaction('👎')
        await message.add_reaction('🤷')


async def setup(bot):
    await bot.add_cog(Poll(bot))
