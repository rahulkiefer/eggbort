# discord.py imports
import discord
from discord.ext import commands

class Help(commands.Cog):
  """
  Commands related to giving bot command descriptions.
  """

  def __init__(self, bot):
    self.bot = bot

  # TODO make 'help' send an embedded message in the server
  @commands.command
  async def help(self, ctx, *args):
    """
    Sends an embedded message in the text channel explaining all bot commands.

    If the call has a command as an argument, it gives the explanation of that
    command within the text channel it was invoked from.
    """
    pass

# TODO make helper function(s) for creating embeds
# should this ^ be a class in a separate file? (Tools? etc.)

def setup(bot):
  bot.add_cog(Help(bot))
