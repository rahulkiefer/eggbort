# # discord.py imports
# import discord
# from discord.ext import commands


# class Events(commands.Cog):

#     def __init__(self, bot):
#         self.bot = bot

#     @commands.Cog.listener()
#     async def on_command_error(self, ctx, error):
#         """
#         Alerts the user if a nonexistent command is used.

#         The alert message disappears after five seconds.
#         """

#         if isinstance(error, commands.CommandNotFound):
#             message = await ctx.send('Invalid command')
#             await message.delete(delay=5)


# def setup(bot):
#     bot.add_cog(Events(bot))
