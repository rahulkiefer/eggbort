# standard imports
import io
import logging
import random
import string

# discord.py imports
import discord
from discord import app_commands
from discord.ext import commands

# external packages
import aiohttp
import requests


class Fun(commands.Cog):
    """
    Misceallaneous commands for fun things.
    """

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='imgur', description="Displays a random image from imgur (potentially NSFW).", nsfw=True)
    async def imgur(self, interaction: discord.Interaction):
        """Displays a random image from imgur (potentially NSFW)."""
        url = self.imgur_url_gen()

        # regenerate random URLs until a valid one is found
        invalid_url: bool = True
        while invalid_url:
            response: requests.Response = requests.get(url)
            if response.url == 'https://i.imgur.com/removed.png':
                url = self.imgur_url_gen()
            else:
                invalid_url = False

        # send the image
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return await interaction.response.send_message("Could not download file...")          

                data = io.BytesIO(await response.read())
                await interaction.response.send_message(
                    file=discord.File(data, url)
                )

    def imgur_url_gen(self) -> str:
        """Generates a random imgur image url."""
        url = 'https://i.imgur.com/'
        url += ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(5))    # the size of the random string can also be 7 chars
        url += '.jpg'
        return url


async def setup(bot):
    await bot.add_cog(Fun(bot))