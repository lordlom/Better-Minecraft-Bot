import discord
from discord.ext import commands
import asyncio
from time import ctime
import logging

class msglogging(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(ctx, message):
        with open("log.txt", "a+") as f:
            f.writelines(f'{ctime()}: {message.author}: {message.content}\n  ')
            print(f'{ctime()}: {message.author}: {message.content} ')

def setup(bot):
    bot.add_cog(msglogging(bot))
    print('\'msglogging\' is loaded')
