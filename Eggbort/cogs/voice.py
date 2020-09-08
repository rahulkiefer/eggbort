import discord
from discord.ext import commands


class Voice(commands.Cog):  # TODO add 'wakeup' to help embeds
    '''Useful commands for certain situations.'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['wake'])
    @commands.has_permissions(move_members=True)
    async def wakeup(self, ctx, username: discord.Member, *,
                     dest_channel: discord.VoiceChannel):
        '''Moves a user back-and-forth between two channels.
        
        The sound that Discord plays when moving a user can be used to get their
        attention if they are deafened in a voice call.
        '''
        invoker_channel = ctx.message.author.voice.channel

        if invoker_channel is not None:
            user_to_move = ctx.message.mentions[0]
            
            if (user_to_move.voice.channel is not None and
                user_to_move.voice.channel == invoker_channel):

                # check if bot is allowed to move users to dest_channel
                # taken care of in error handling

                # check if invoker is allowed to move users to dest_channel
                # TODO if ever necessary

                for _ in range(5):
                    await user_to_move.move_to(dest_channel)
                    await user_to_move.move_to(invoker_channel)
            else:
                await ctx.send(
                    f'{user_to_move.name} is not in your voice channel.'
                )
        else:
            await ctx.send(
                'You must be in the same voice channel as the specified user.'
            )

    @wakeup.error
    async def wakeup_error(self, ctx, error):
        # if the voice channel is restricted to those with a certain server role
        if isinstance(error, commands.BotMissingRole):
            await ctx.send(
                'I do not have permissions to move users into that channel.'
            )


def setup(bot):
    bot.add_cog(Voice(bot))
