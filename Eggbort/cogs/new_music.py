"""discord.py imports"""
import wavelink
from discord.ext import commands

# TODO will have to find the new way to implement this with slash commands


class NewMusic(commands.Cog):
    """Updated commands that relate to playing music."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: str) -> None:
        """Simple play command."""

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        track = await wavelink.YouTubeTrack.search(search, return_first=True)
        await vc.play(track)

    @commands.command()
    async def disconnect(self, ctx: commands.Context) -> None:
        """Simple disconnect command.

        This command assumes there is a currently connected Player.
        """
        vc: wavelink.Player = ctx.voice_client
        await vc.disconnect()


async def setup(bot: commands.Bot):
    """Adds the NewMusic cog"""
    await bot.add_cog(NewMusic(bot))
