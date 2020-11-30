import discord
from discord.ext import commands
import hypixel

@commands.command()
async def level(ctx, name):
    level = hypixel.get_level(name)
    if level is None:
        await ctx.send("Player not found! (Make sure to use their **Minecraft** username)")
    else:
        await ctx.send(f"Level of user {name}: {level}")

def setup(bot):
    bot.add_cog(hypixel(bot))
    print('\'hypixel\' is loaded')
