# discord.py imports
import discord
from discord.ext import commands


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


help_embed = discord.Embed(
                title='Eggbort Commands',
                description='Call help on specific commands to get more info.',
                color=discord.Color.gold(),
            )

# TODO get link to eggbort's avatar
help_embed.set_footer(text="Eggbort Commands")
# help_embed.set_thumbnail(url=[LINK TO EGGBORT AVATAR PNG])

# COG descriptions vvv

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

    # TODO make 'help' send an embedded message in the server
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
