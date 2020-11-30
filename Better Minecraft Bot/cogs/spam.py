import discord
import asyncio
import datetime
import os
import time
from discord.ext import commands
from discord import Embed
import subprocess

class spammer(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command('spam')
    @commands.has_permissions(administrator=True)
    async def spam(self, ctx, payload: str, spamtime: int):
        await ctx.channel.purge(limit=1)
        for i in range(spamtime):
            await ctx.send(payload)

'''
@commands.command()
async def dmSpam(self, ctx, payload: str, spamtime: int):
    await ctx.channel.purge(limit=1)
    userid = [
            736455350105931809,
            328977584236789781,
            518497307977580567,
            433425654705291276,
            756272309161164891,
            563019517718953993,
            559815467779358720,
            760194474205773864,
            689499715016196180,
            617518482124439564,
            496347465004351498,
            619774087949975553,
            716133197926367365,
            631654995854491658,
            534421240996167703
                ]
    for user in userid:
        senduser = await self.bot.get_user_info(user_id = user)
        for i in range(spamtime):
            await bot.send_message(senduser, payload)
'''
@commands.command(name='ghostping')
async def ghostping(self, ctx, pingnum: int):
    for i in range(pingnum):
        await ctx.send('@everyone')
        await ctx.channel.purge(limit = 1)

def setup(bot):
    bot.add_cog(spammer(bot))
    print('\'spammer\' is loaded')
