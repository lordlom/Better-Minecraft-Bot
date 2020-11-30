import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil

class voice(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    global queues
    queues = {}

    @commands.command(aliases=['join', 'j'])
    async def cjoin(self, ctx):
        #try:
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)

        else:
            await channel.connect()
            print(f'I have connected to {channel}')

        await ctx.send(f'POG I am in {channel}')

        #except:
        #    await ctx.send('cant join a channel you are not in')
        #    print('join called while user not in channel')

    @commands.command(aliases=['leave','l'])
    async def cleave(self, ctx):
        try:
            global voice
            channel = ctx.message.author.voice.channel
            voice = get(self.bot.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():
                await voice.disconnect()
                print('I have left')
                await ctx.send('Leaving...')
            else:
                print('Issues have prevented me from leaving :()')
                await ctx.send('Wh- What are you doing? I am not even in the channel')
                await voice.disconnect()

        except:
            await ctx.send('cannot leave when not in a channel')
            print('leave called while not in a channel')

    @commands.command(aliases=['play','p'])
    async def cplay(self, ctx, url: str):

        def check_queue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath('Queue'))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print('no songs in queue')
                    queues.clear()
                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                song_path = os.path.abspath(os.path.realpath('Queue') + '\\' + first_file)
                if length != 0:
                    print('song done reading queue')
                    print(f'songs remaining{still_q}')
                    song_there = os.path.isfile('song.mp3')
                    if songthere:
                        os.remove('song.mp3')
                        shutil.move(song_path, main_location)
                        for file in os.listdir('./'):
                            if file.endswith('.mp3'):
                                os.rename(file, 'song.mp3)')

                        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                        voice.source = discord.PCMVolumeTransformer(voice.source)
                        voice.source.volume = 0.10
                    else:
                        queues.clear()
                        return
                else:
                    queues.clear()
                    print('no new songs queued')

        song_there = os.path.isfile("song.mp3")

        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")

        except PermissionError:
            print("Trying to delete song file, but it's being played")
            await ctx.send("ERROR: Music playing")
            return

        await ctx.send("Getting everything ready now")

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.25

        nname = name.rsplit("-", 2)
        await ctx.send(f"Playing: {nname[0]}")
        print("playing\n")

    @commands.command(aliases=['pause'])
    async def cpause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            await ctx.send('Music paused')
            print('Music paused')
            voice.pause()
        else:
            print('pause called but no music playing\n')
            await ctx.send('couldnt pause music as none is playing')

    @commands.command(aliases=['resume', 'unpause'])
    async def cresume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_paused():
            await ctx.send('Music resumed')
            print('Music resumed')
            voice.resume()
        else:
            print('resumed called but no music paused\n')
            await ctx.send('couldnt resume music as none is paused')

    @commands.command()
    async def tts(self, ctx, say):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        say = say.replace('#', ' ')
        tts = gTTS(say)
        tts.save('ttssay.mp3')

        voice.play(discord.FFmpegPCMAudio("ttssay.mp3"), after=lambda e: print("tts done!"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.50

    @commands.command(aliases=['skip', 'stop','s'])
    async def cstop(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        queues.clear()

        if voice and voice.is_playing():
            await ctx.send('Music skipped')
            print('Music stopped')
            voice.stop()
        else:
            print('call to stop but no music playing\n')
            await ctx.send('cant stop music as none is playing')

    @commands.command(aliases=['q', 'queue'])
    async def cqueue(self, ctx, url: str):
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is False:
            os.mkdir("Queue")
        DIR = os.path.abspath(os.path.realpath("Queue"))
        q_num = len(os.listdir(DIR))
        q_num += 1
        add_queue = True
        while add_queue:
            if q_num in queues:
                q_num += 1
            else:
                add_queue = False
                queues[q_num] = q_num

        queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': queue_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
        await ctx.send("Adding song " + str(q_num) + " to the queue")

        print("Song added to queue\n")

def setup(bot):
    bot.add_cog(voice(bot))
    print('\'voice\' is loaded')
