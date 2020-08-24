from discord.ext import commands


class UserInfo(commands.Cog):
    '''Commands related to retrieving user info.'''

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def avatar(self, ctx):
        '''Sends the user's avatar.'''
        url = str(ctx.message.mentions[0].avatar_url) + '?size=256'
        await ctx.send(url)

    @commands.command()
    async def joindate(self, ctx):
        '''Gives the date the member first joined the server (UTC format).'''
        await ctx.send(ctx.message.mentions[0].joined_at)


def setup(bot):
    bot.add_cog(UserInfo(bot))