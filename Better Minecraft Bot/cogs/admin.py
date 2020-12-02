import discord
import asyncio
import datetime
import os
import time
from discord.ext import commands
from discord import Embed
import subprocess

class admin(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, cog: str):
        if 'admin' not in cog:
            try:
                self.bot.unload_extension(cog)
            except Exception as e:
                await ctx.send(f'ERROR 404 {cog} NOT FOUND')
                return
            await ctx.send('COG UNLOADED SUCESSFULLY')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'ERROR 404 {cog} NOT FOUND')
            return
        await ctx.send('COG LOADED SUCESSFULLY')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            await ctx.send(f'RELOADING... RELOADING... RELOADING...')
            time.sleep(1)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'ERROR 404 COULD NOT LOAD {cog}')
            return
        await ctx.send('COG RELOADED SUCESSFULLY')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target: discord.member):
        await self.bot.kick(target)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        time.sleep(.3)
        await ctx.channel.purge(limit = limit + 1)

    @commands.command()
    async def botsay(self, ctx, message: str):
        channel = self.bot.get_channel(782385370850525257)
        await channel.send(message)

    @commands.command()
    async def github(self, ctx):
        await ctx.send('https://github.com/lordlom/Better-Minecraft-Bot')

def setup(bot):
    bot.add_cog(admin(bot))
    print('\'admin\' is loaded')
