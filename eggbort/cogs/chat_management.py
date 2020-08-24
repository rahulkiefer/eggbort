from discord.ext import commands


class ChatManagement(commands.Cog):
    """
    Commands related to managing chat.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, n_messages=1):
        """
        Deletes the given number of messages above (default is 1)

        By default, with no number given, the clear command itself and the
        message above it will be deleted.
        """
        if n_messages < 1:
            msg = await ctx.send('Cannot clear less than 1 message.')
            await msg.delete(delay=1)
        else:
            await ctx.channel.purge(limit=n_messages + 1)


def setup(bot):
    bot.add_cog(ChatManagement(bot))
