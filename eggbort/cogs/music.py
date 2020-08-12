# Built-in library imports
import asyncio

# discord.py imports
import discord
from discord.ext import commands

# misc imports
import youtube_dl

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


# TODO add 'pause' and 'skip' options
# TODO add listing first N (5?) results on youtube query to choose from there
#      when no link is provided


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    # bind to ipv4 since ipv6 addresses cause issues sometimes
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(
            None,
            lambda: ytdl.extract_info(url, download=not stream)
        )

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(
            discord.FFmpegPCMAudio(
                filename,
                **ffmpeg_options),
            data=data)


# TODO after implementing Rapptz' basic music file, implement queueing
# using Lucas' video
class Music(commands.Cog):
    """
    Events/commands related to playing music.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, url: str):
        """Plays the audio of a YouTube video, given the URL.

        If the bot is not already in the user's voice channel, it will join that
        channel and start playing audio.
        """
        channel = ctx.message.author.voice.channel

        ### JOIN #######

        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(channel)
        else:
            await channel.connect()  # creates a Discord voice connection

        ### JOIN END ###

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(
                player,
                after=lambda e: print('Player error: %s' % e) if e else None
            )

        await ctx.send('Now playing: {}'.format(player.title))

        # TODO add music to queue?

    @commands.command()
    async def stop(self, ctx):
        """Disconnects the bot from the voice channel."""

        await ctx.voice_client.disconnect()

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume."""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))


def setup(bot):
    bot.add_cog(Music(bot))
