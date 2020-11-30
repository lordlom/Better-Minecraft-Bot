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
        channel = self.bot.get_channel(742122497146748988)
        await channel.send(message)

    @commands.command()
    async def changenick(self, ctx, member: str, newname: str):
        await ctx.author.edit(nick=newname)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()

            # this also works
            await message.channel.send('Goodbye in 3 seconds...', delete_after=3.0)

    async def on_message_delete(self, message):
        fmt = '{0.author} has deleted the message: {0.content}'
        await message.channel.send(fmt.format(message))

        async def on_message(self, message):
            if message.author.id == self.user.id:
                return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

async def ex(args, message, client, invoke):

    try:
        ammount = int(args[0]) + 1 if len(args) > 0 else 2
    except:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), descrition="Please enter a valid value for message ammount!"))
        return

    cleared = 0
    failed = 0

    async for m in client.logs_from(message.channel, limit=ammount):
        try:
            await client.delete_message(m)
            cleared += 1
        except:
            failed += 1
            pass

    failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""
    returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s).%s" % (cleared, failed_str)))
    await asyncio.sleep(4)
    await client.delete_message(returnmsg)

    @client.command()

    async def kick(ctx, member: discord.Member, *, reason=None):

        await member.kick(reason=reason)

        await ctx.send(f'User {member} has been kicked.')

def setup(bot):
    bot.add_cog(admin(bot))
    print('\'admin\' is loaded')
