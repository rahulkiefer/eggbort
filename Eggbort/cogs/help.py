"""discord.py imports"""
from discord import Embed, Color
from discord.ext import commands

# dictionary of all individual bot command embeds
eggbort_commands = {
    # Bot Properties
    'ping': Embed(
        title='ping',
        description='''
                            Displays the bot's latency.

                            `e.ping`
                            ''',
        color=Color.green(),
    ),
    # Chat Management
    'clear': Embed(
        title='clear',
        description='''
                            Deletes the given number of messages.
                            Arguments:
                            amount (default: 1)

                            `e.clear [amount]`
                            ''',
        color=Color.lighter_grey(),
    ).add_field(
        name='Aliases',
        value='delete',
    ),
    # Help
    'help': Embed(
        title='help',
        description='''
                            Gives bot command descriptions.
                            Arguments:
                            command (optional | default: None)

                            `e.help [command]`
                            ''',
        color=Color.purple(),
    ),
    # Music
    'connect': Embed(
        title='connect',
        description='''
                            Connect to a voice channel.

                            `e.connect`
                            ''',
        color=Color.red(),
    ),
    'play': Embed(
        title='play',
        description='''
                            Play or queue a song with the given query.
                            Arguments:
                            query (default: None)

                            `e.play [query]`
                            ''',
        color=Color.red(),
    ),
    'pause': Embed(
        title='pause',
        description='''
                            Pause the currently playing song.

                            `e.pause`
                            ''',
        color=Color.red(),
    ),
    'resume': Embed(
        title='resume',
        description='''
                            Resume a currently paused player.

                            `e.resume`
                            ''',
        color=Color.red(),
    ),
    'skip': Embed(
        title='skip',
        description='''
                            Skip the currently playing song.

                            `e.skip`
                            ''',
        color=Color.red(),
    ),
    'stop': Embed(
        title='stop',
        description='''
                            Stop the player and clear all internal states.

                            `e.stop`
                            ''',
        color=Color.red(),
    ),
    'volume': Embed(
        title='volume',
        description='''
                            Change the player's volume, between 1 and 100.
                            Arguments:
                            volume (default: None)

                            `e.volume [volume]`
                            ''',
        color=Color.red(),
    ).add_field(
        name='Aliases',
        value='v, vol',
    ),
    'shuffle': Embed(
        title='shuffle',
        description='''
                            Shuffle the player's queue.

                            `e.shuffle`
                            ''',
        color=Color.red(),
    ).add_field(
        name='Aliases',
        value='mix',
    ),
    'equalizer': Embed(
        title='equalizer',
        description='''
                            Change the player's equalizer.
                            Arguments:
                            equalizer (default: None)

                            `e.equalizer`
                            ''',
        color=Color.red(),
    ).add_field(
        name='Aliases',
        value='eq',
    ),
    'queue': Embed(
        title='queue',
        description='''
                            Display the player's queued songs.

                            `e.queue`
                            ''',
        color=Color.red(),
    ).add_field(
        name='Aliases',
        value='q, que',
    ),
    'nowplaying': Embed(
        title='nowplaying',
        description='''
                            Update the player controller.

                            `e.nowplaying`
                            ''',
        color=Color.red(),
    ).add_field(
        name='Aliases',
        value='np, now_playing, current',
    ),
    'swap_dj': Embed(
        title='nowplaying',
        description='''
                            Swap the current DJ to another member in the voice channel.
                            Arguments:
                            user (default: None)

                            `e.swap_dj <@user>`
                            ''',
        color=Color.red(),
    ).add_field(
        name='Aliases',
        value='swap',
    ),
    # Poll
    'poll': Embed(
        title='poll',
        description='''
                            Creates a poll using reactions on the message.
                            Arguments:
                            message (optional | default: None)

                            `e.poll [message]`
                            ''',
        color=Color.red(),
    ),
    # User Info
    'avatar': Embed(
        title='avatar',
        description='''
                            Sends the avatar of the specified user.
                            Arguments:
                            user

                            `e.avatar <@user>`
                            ''',
        color=Color.blue(),
    ).add_field(
        name='Aliases',
        value='pfp',
    ),
    'joindate': Embed(
        title='joindate',
        description='''
                            Gives the date the user first joined the server.
                            Arguments:
                            user

                            `e.joindate <@user>`
                            ''',
        color=Color.blue(),
    ),
}


# embed for overall help command call
help_embed = Embed(
    title='Eggbort Commands',
    description='Call help on specific commands to get more info.',
    color=Color.gold(),
)

help_embed.set_footer(
    text='Bot developed by rdk750#9435',
    icon_url='https://cdn.discordapp.com/avatars/220377491926286337/786637c4ef148510dcbe13b865f3e0ea.png?size=256'
)

help_embed.set_thumbnail(
    url='https://cdn.discordapp.com/avatars/728707277489569902/fd9afd578e4c4a8b6d4b947e09cf4e28.png'
)

help_embed.add_field(
    name='❓ Help',
    value='• help [command]',
    inline=True,
)

help_embed.add_field(
    name='🛠️ Bot Properties',
    value='''
            • ping
            ''',
    inline=True,
)

help_embed.add_field(
    name='📝 Chat Management',
    value='• clear [amount]',
    inline=True,
)

help_embed.add_field(
    name='🎵 Music',
    value='''
            • connect
            • play [query]
            • pause
            • resume
            • skip
            • stop
            • volume [volume]
            • shuffle
            • equalizer [equalizer]
            • queue
            • nowplaying
            • swap_dj <@user>
            ''',
    inline=True,
)

help_embed.add_field(
    name='📊 Poll',
    value='''
            • poll [message]
            ''',
    inline=True,
)

help_embed.add_field(
    name='ℹ️ User Info',
    value='''
            • avatar <@user>
            • joindate <@user>
            ''',
    inline=True,
)


class Help(commands.Cog):
    """
    Commands related to giving bot command descriptions.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *args):
        """
        Sends an embedded message in the text channel explaining all bot commands.

        If the call has a command as an argument, it gives the explanation of that
        command within the text channel it was invoked from.
        """
        if len(args) > 0:
            cmd = ' '.join(args)

            await ctx.send(
                embed=eggbort_commands.get(
                    cmd,
                    Embed(description=f'{cmd} is not a command.')
                )
            )

        else:
            await ctx.send(embed=help_embed)


async def setup(bot):
    """Adds the Help cog"""
    bot.remove_command('help')  # removes default help command
    await bot.add_cog(Help(bot))
