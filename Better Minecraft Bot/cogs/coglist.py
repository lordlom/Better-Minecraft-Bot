import discord
import asyncio
import datetime
from discord.ext import commands
from discord import Embed
import json
import os
import datetime

class coglist(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def coglist(self, ctx):
        with open("coglist.json") as f:
            data = json.load(f)

        embed = discord.Embed(color=(0x84fa), url="https://discordapp.com/", description="Coglist")
        for i in range(len(data["commands"])):
            embed.add_field(name=data['commands'][i]["name"], value=data["commands"][i]["functions"],inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(coglist(bot))
    print('\'coglist\' is loaded')
