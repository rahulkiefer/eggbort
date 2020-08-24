# discord.py imports
import discord
from discord.ext import commands  # TODO add in User Info commands

# dictionary of all individual bot command embeds
eggbort_commands = {
    # Bot Properties
    'ping': discord.Embed(
                title='ping',
                description='''
                            Displays the bot's latency.

                            `e.ping`
                            ''',
                color=discord.Color.green(),
            ),
    # Chat Management
    'clear': discord.Embed(
                title='clear',
                description='''
                            Deletes the given number of messages.
                            Arguments:
                            amount (default: 1)

                            `e.clear [amount]`
                            ''',
                color=discord.Color.lighter_grey(),
            ),
    # Help
    'help': discord.Embed(
                title='help',
                description='''
                            Gives bot command descriptions.
                            Arguments:
                            command (optional | default: None)

                            `e.help [command]`
                            ''',
                color=discord.Color.purple(),
            ),
    # Poll
    'poll': discord.Embed(
                title='poll',
                description='''
                            Creates a poll using reactions on the message.
                            Arguments:
                            message (optional | default: None)

                            `e.poll [message]`
                            ''',
                color=discord.Color.red(),
            ),
}


# embed for overall help command call
help_embed = discord.Embed(
                title='Eggbort Commands',
                description='Call help on specific commands to get more info.',
                color=discord.Color.gold(),
            )

help_embed.set_footer(
    text='Bot by rdk750#9435',
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
    name='📊 Poll',
    value='''
            • poll [message]
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
            cmd = args[0]

            await ctx.send(
                embed=eggbort_commands.get(
                          cmd,
                          discord.Embed(description=f'{cmd} is not a command.')
                )
            )

        else:
            await ctx.send(embed=help_embed)


def setup(bot):
    bot.remove_command('help')  # removes default help command
    bot.add_cog(Help(bot))
