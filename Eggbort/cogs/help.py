# discord.py imports
from discord import Embed, Color
from discord.ext import commands


class HelpEmbed(Embed):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = Color.from_rgb(255, 215, 154)
        self.set_footer(
            text='Bot developed by rdk750#9435',
            icon_url='https://cdn.discordapp.com/avatars/220377491926286337/786637c4ef148510dcbe13b865f3e0ea.png?size=256'
        )


class CustomHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        """Sends all command categories and lists the commands within each"""
        embed = HelpEmbed(title='Eggbort Help')
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/728707277489569902/fd9afd578e4c4a8b6d4b947e09cf4e28.png')

        # TODO use cog.get_app_commands() to get all slash commands defined instead??
        for cog, commands in mapping.items():
            if filtered_commands := await self.filter_commands(commands):
                # if no commands are usable in this category, don't want to display it
                if cog:
                    name = cog.qualified_name
                    desc = cog.description or "No description"

                    cmd_list = [f'• {cmd}' for cmd in commands]

                    embed.add_field(
                        name=cog.qualified_name,
                        value='\n'.join(cmd_list),
                        inline=True
                    )


        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        """Triggers when a `<prefix>help <cog>` is called"""
        embed = HelpEmbed(
            title=cog.qualified_name,
            description=cog.description
        )
        
        cmd_list = [f'• {cmd}' for cmd in cog.get_app_commands()]

        for slash_cmd in cog.get_app_commands():
            embed.add_field(
                name=slash_cmd.name,
                value=slash_cmd.description
            )

        await self.get_destination().send(embed=embed)
    
    async def send_command_help(self, command):
        """Explains the usage of a specific command"""
        embed = HelpEmbed(
            title=command.qualified_name,
            description=command.help    # gets description from function docstring
        )

        await self.get_destination().send(embed=embed)


class Help(commands.Cog):
    """
    Help commands for the bot.
    """
    def __init__(self, bot):
        self.bot = bot

        help_command = CustomHelp()
        help_command.cog = self
        bot.help_command = help_command


async def setup(bot):
    await bot.add_cog(Help(bot))
