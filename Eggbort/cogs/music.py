# discord.py imports
import discord
from discord import app_commands
from discord.ext import commands

# external packages
import wavelink


class Music(commands.Cog):  # TODO add functionality for Spotify and Soundcloud tracks in the play command
    """Commands that relate to playing music."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='play', description="Play a song")
    @app_commands.checks.has_permissions(speak=True)
    async def play(self, interaction: discord.Interaction, query: str):
        """Play a song with the given search query.

        If not connected, connect to our voice channel.
        """
        if interaction.user.voice is None:
            return await interaction.response.send_message("You are not in a voice channel.", ephemeral=True, delete_after=5)
        vc: wavelink.Player = interaction.guild.voice_client or await interaction.user.voice.channel.connect(cls=wavelink.Player, self_deaf=True)

        track = await wavelink.YouTubeTrack.search(query, return_first=True)

        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(track)
            await interaction.response.send_message(f'Playing `{track.title}`.')
        else:
            await vc.queue.put_wait(track)
            await interaction.response.send_message(f'Added `{track.title}` to the queue...', delete_after=10)

    @app_commands.command(name='pause', description="Pause the player") # TODO can I delete the message after playing is resumed?
    @app_commands.checks.has_permissions(speak=True)
    async def pause(self, interaction: discord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if vc.is_paused():
            await interaction.response.send_message(f"Player is already paused.", ephemeral=True, delete_after=5)
        elif vc.is_playing():
            await vc.pause()
            await interaction.response.send_message(f"Paused player.")
        else:
            await interaction.response.send_message(f"Not currently playing a song.", ephemeral=True, delete_after=5)

    @app_commands.command(name='resume', description="Resume the player")
    @app_commands.checks.has_permissions(speak=True)
    async def resume(self, interaction: discord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if vc.is_paused():
            await vc.resume()
            await interaction.response.send_message(f"Resumed playing: `{vc.current}`", delete_after=5)
        else:
            await interaction.response.send_message(f"Player is not paused.", ephemeral=True, delete_after=5)

    @app_commands.command(name='skip', description="Skips the current song in the queue")
    @app_commands.checks.has_permissions(speak=True)
    async def skip(self, interaction: discord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if not vc.queue.is_empty:
            await vc.stop()
            await interaction.response.send_message(f"Now playing: `{vc.queue[0]}`", delete_after=5)

    @app_commands.command(name='stop', description="Stops playing and clears queue")
    @app_commands.checks.has_permissions(speak=True)
    async def stop(self, interaction: discord.Interaction):
        vc: wavelink.Player = interaction.guild.voice_client
        if vc.is_playing():
            await vc.stop()
            await interaction.response.send_message("Stopped player.")
        else:
            await interaction.response.send_message("No songs are currently playing.", delete_after=5)

    @app_commands.command(name='disconnect', description="Leave a voice channel")
    @app_commands.checks.has_permissions(speak=True)
    async def disconnect(self, interaction: discord.Interaction):
        """Leave a voice channel."""
        if vc := interaction.guild.voice_client:
            await vc.disconnect()
            await interaction.response.send_message("Disconnected.", delete_after=5)
        else:
            await interaction.response.send_message("Not currently in a voice channel.", ephemeral=True, delete_after=5)

    # @app_commands.command(name='connect', description="Join a voice channel.")
    # @app_commands.checks.has_permissions(speak=True)
    # async def connect(self, interaction: discord.Interaction):
    #     """Join a voice channel."""
    #     vc: wavelink.Player = await interaction.user.voice.channel.connect(cls=wavelink.Player, self_deaf=True)  # type: ignore
    #     await interaction.response.send_message("Connected.")
    #     return vc

    # OLD PLAY CMD
    # @app_commands.command(name='play', description="Searches YouTube for the provided query/link and plays the video's audio.")  # TODO update description when spotify compatibility is added
    # @app_commands.checks.has_permissions(speak=True)
    # async def play(self, interaction: discord.Interaction, query: str) -> None:
    #     """Searches YouTube for the provided query/link and plays the video's audio."""
    #     if not interaction.user.voice:
    #         return await interaction.response.send_message("You are not in a voice channel.", ephemeral=True, delete_after=5)

    #     if not interaction.guild.voice_client:
    #         vc: wavelink.Player = await interaction.user.voice.channel.connect(cls=wavelink.Player, self_deaf=True)
    #     else:
    #         vc: wavelink.Player = interaction.guild.voice_client

    #     track = await wavelink.YouTubeTrack.search(query, return_first=True)
    #     await vc.play(track)
    #     await interaction.response.send_message(f"`Playing {query}.`")

    # https://beta.mystb.in/EquivalentRopeIncidents


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
