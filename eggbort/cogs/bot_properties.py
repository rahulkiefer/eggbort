# Built-in library imports
import json

# Discord library imports
import discord
from discord.ext import commands

# My file imports
import file_paths


class BotProperties(commands.Cog):
  """
  Events/commands related to monitoring/altering the bot's properties.
  """

  def __init__(self, bot):
    self.bot = bot


  ##### EVENTS #################################################################

  @commands.Cog.listener()
  async def on_ready(self):
    """Sets the bot's status and activity upon booting up"""
    
    await self.bot.change_presence(
      status = discord.Status.online,
      activity = discord.Activity(
        type = discord.ActivityType.playing,
        name = 'egg!help'
      )
    )
    print('Bot is ready.')  # for debugging purposes

  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    """Adds the 'egg!' server prefix upon joining a server."""

    with open(file_paths.SERVER_PREFIXES, 'r') as f:
      server_prefixes = json.load(f)

    server_prefixes[str(guild.id)] = 'egg!'  # default bot prefix

    with open(file_paths.SERVER_PREFIXES, 'w') as f:
      json.dump(server_prefixes, f, indent=4)

  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    """Removes current server prefix upon leaving a server."""

    with open(file_paths.SERVER_PREFIXES, 'r') as f:
      server_prefixes = json.load(f)

    del server_prefixes[str(guild.id)]

    with open(file_paths.SERVER_PREFIXES, 'w') as f:
      json.dump(server_prefixes, f, indent=4)


  ##### COMMANDS ###############################################################

  @commands.command()
  async def ping(self, ctx):
    """Displays the bot's latency"""
    await ctx.send('Latency: {} ms'.format(round(self.bot.latency * 1000)))

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def serverprefix(self, ctx, *args):
    """
    Shows (changes) the server prefix (w/ argument)
    
    If the call has an argument, changes the prefix to the argument.
    """

    with open(file_paths.SERVER_PREFIXES, 'r') as f:
      server_prefix = json.load(f)

    new_prefix = ' '.join(args)

    # if an argument for serverprefix has been given, set it as the new prefix
    if new_prefix != '':
      server_prefix[str(ctx.guild.id)] = new_prefix

      with open(file_paths.SERVER_PREFIXES, 'w') as f:
        json.dump(server_prefix, f, indent=4)

      await ctx.send('Server prefix has been updated to: {}'.format(new_prefix))
      
    else:
      await ctx.send(
        'Current server prefix is: {}'.format(
          server_prefix[str(ctx.guild.id)]
        )
      )


def setup(bot):
  bot.add_cog(BotProperties(bot))
