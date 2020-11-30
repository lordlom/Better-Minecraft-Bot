import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil
import random
import time

class dice(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(aliases=['r'])
    async def roll(self, ctx, dnum: str, roletime: int = 1):
        if roletime < 20:
            for i in range(roletime):
                dnum = dnum.replace('d', '')
                r = random.randint(1, int(dnum))
                await ctx.send('rolling dice...')
                time.sleep(.3)
                await ctx.send(r)
        else:
            await ctx.send(f'the amount of times to role is too high, {ctx.message.author}.')

def setup(bot):
    bot.add_cog(dice(bot))
    print('\'dice\' is loaded')
