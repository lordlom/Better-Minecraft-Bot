import logging
import discord
import time
import asyncio
from typing import Optional
from pathlib import Path
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CheckFailure
from discord.ext.commands import has_permissions, bot_has_permissions
from discord.ext.commands import Greedy
from discord import Embed
import datetime
import json
import sys
import traceback


client = commands.Bot(command_prefix='./', case_insensitive=True)

client.remove_command('help')

initial_extensions = [
                        'cogs.admin',
                        'cogs.voice',
                        'cogs.msglogging',
                        'cogs.dice',
                        'cogs.help',
                        'cogs.spam',
                        'cogs.hypixel'
                     ]

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Minecraft Bot is my bad younger cousin'))
    print(f'logged in as {client.user.name} - {client.user.id}')

client.run('Token')
