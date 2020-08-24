# built-in library imports
import io

# discord.py imports
import discord.file
from discord.ext import commands

# external packages
import aiohttp


class UserInfo(commands.Cog):
    '''Commands related to retrieving user info.'''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx):
        '''Sends the user's avatar.'''
        user = ctx.message.mentions[0]
        url = f'{user.avatar_url}?size=256'

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(
                    file=discord.File(data, f'{user.name}_avatar.jpg')
                )

    @commands.command()
    async def joindate(self, ctx):
        '''Gives the date the member first joined the server (UTC format).'''
        await ctx.send(ctx.message.mentions[0].joined_at)


def setup(bot):
    bot.add_cog(UserInfo(bot))
