import discord
from discord.ext import commands

# TODO make this cog with basic youtube audio playback functionality
class Music(commands.Cog):
  """
  Events/commands related to playing music.
  """

  def __init__(self, bot):
    self.bot = bot


def setup(bot):
  bot.add_cog(Music(bot))