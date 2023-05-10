# discord.py imports
import discord
from discord import app_commands
from discord.ext import commands

# external packages
import wavelink


class CustomPlayer(wavelink.Player):
    """Custom player class."""
    def __init__(self):
        super().__init__()
        self.autoplay=True


class Music(commands.Cog):  # TODO add functionality for Spotify and Soundcloud tracks in the play command
    """Commands that relate to playing music."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.player = CustomPlayer()

    @app_commands.command(name='play', description="Play a song")
    @app_commands.checks.has_permissions(speak=True)
    async def play(self, interaction: discord.Interaction, query_or_link: str):
        """Play a song with the given search query.

        If not connected, connect to our voice channel. If a YouTube playlist 
        link is specified, queues all tracks in the playlist.
        """
        if interaction.user.voice is None:
            return await interaction.response.send_message("You are not in a voice channel.", ephemeral=True, delete_after=5)
        vc: CustomPlayer = interaction.guild.voice_client or await interaction.user.voice.channel.connect(cls=self.player, self_deaf=True)

        if query_or_link.startswith('https://www.youtube.com/playlist'):
            await self.playYouTubePlaylist(interaction, self.player, query_or_link)
        else:
            track = await wavelink.YouTubeTrack.search(query_or_link, return_first=True)

            if vc.queue.is_empty and not vc.is_playing():
                await vc.play(track)
                await interaction.response.send_message(f'Playing `{track.title}` by `{track.author}`.')
            else:
                await vc.queue.put_wait(track)
                await interaction.response.send_message(f'Added `{track.title}` by `{track.author}` to the queue.', delete_after=10)

    async def playYouTubePlaylist(self, interaction: discord.Interaction, vc: CustomPlayer, link: str):
        embed = discord.Embed(description="Searching", color=discord.Color.from_str("rgb(0,0,0)"))
        await interaction.response.send_message(embed=embed)
        try:
            embed = discord.Embed(description=f"[Playlist added to queue]({link})", color=discord.Color.from_str("rgb(0,0,0)"))
            playlist = await wavelink.YouTubePlaylist.search(link)
            tracks: list[wavelink.YouTubeTrack] = playlist.tracks
            songs = len(tracks)
            length = sum(track.length for track in tracks)
            if not vc.is_playing():
                for track in tracks:
                    vc.queue.put(track)
                first_track = vc.queue.get()
                embed.add_field(name="Now Playing", value=f"{first_track.title} by {first_track.author}")
                embed.set_image(url=first_track.thumbnail)
                await vc.play(first_track)
            else:
                for track in tracks:
                    vc.queue.put(track)
            minutes, seconds = divmod(length / 1000, 60)
            hours, minutes = divmod(minutes, 60)
            if hours > 0:
                duration = f"{int(hours)}:{int(minutes):02d}:{int(seconds):02d}"
            else:
                duration = f"{int(minutes):02d}:{int(seconds):02d}"
            
            embed.add_field(name="Enqueued", value=f"{songs} songs")
            embed.set_footer(text=f"Playlist Duration: {duration}")
            await interaction.edit_original_response(embed=embed)
        except Exception:
            embed = discord.Embed(description=f"{link} is an invalid link/playlist!", color=discord.Color.red())
            await interaction.edit_original_response(embed=embed)

    @app_commands.command(name='pause', description="Pause the player") # TODO can I delete the message after playing is resumed?
    @app_commands.checks.has_permissions(speak=True)
    async def pause(self, interaction: discord.Interaction):
        vc: CustomPlayer = interaction.guild.voice_client
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
        vc: CustomPlayer = interaction.guild.voice_client
        if vc.is_paused():
            await vc.resume()
            await interaction.response.send_message(f"Resumed playing: `{vc.current}`", delete_after=5)
        else:
            await interaction.response.send_message(f"Player is not paused.", ephemeral=True, delete_after=5)

    @app_commands.command(name='skip', description="Skips the current song in the queue")
    @app_commands.checks.has_permissions(speak=True)
    async def skip(self, interaction: discord.Interaction):
        vc: CustomPlayer = interaction.guild.voice_client
        if not vc.queue.is_empty:
            await vc.stop()
            await interaction.response.send_message(f"Now playing: `{vc.queue[0]}`")

    @app_commands.command(name='stop', description="Stops playing and clears queue")
    @app_commands.checks.has_permissions(speak=True)
    async def stop(self, interaction: discord.Interaction):
        vc: CustomPlayer = interaction.guild.voice_client
        if not vc.queue.is_empty:
            vc.queue.clear()
        if vc.is_playing():
            await vc.stop()
            await interaction.response.send_message("Stopped player.")
        else:
            await interaction.response.send_message("No songs are currently playing.", ephemeral=True, delete_after=5)

    @app_commands.command(name='disconnect', description="Leave a voice channel")
    @app_commands.checks.has_permissions(speak=True)
    async def disconnect(self, interaction: discord.Interaction):
        """Leave a voice channel."""
        if vc := interaction.guild.voice_client:
            await vc.disconnect()
            await interaction.response.send_message("Disconnected.", delete_after=5)
        else:
            await interaction.response.send_message("Not currently in a voice channel.", ephemeral=True, delete_after=5)

    @app_commands.command(name='queue', description="Lists the songs in the queue")
    async def queue(self, interaction: discord.Interaction):
        vc: CustomPlayer = interaction.guild.voice_client
        if not vc.queue.is_empty:
            await interaction.response.send_message('\n'.join(f'• `{song}`' for song in vc.queue))
        else:
             await interaction.response.send_message(f"The queue is empty.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
