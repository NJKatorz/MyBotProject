import discord
from discord.ext import commands
import os
import asyncio
import yt_dlp
from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('token_nj')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    voice_clients = {}
    yt_dlp_options = {"format": "bestaudio/best"}
    ytdl = yt_dlp.YoutubeDL(yt_dlp_options)
    
    ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.25"'}
    
    @client.event
    async def on_ready():
        print(f'{client.user} is here !')
        
    @client.event
    async def on_message(message):
        if message.content.startswith("-play"):
            try:
                # Connect to the voice channel
                voice_client = await message.author.voice.channel.connect()
                voice_clients[voice_client.guild.id] = voice_client
            except Exception as e:
                print(f"Error connecting to voice channel: {e}")
                return

            try:
                url = message.content.split()[1]

                # Extract playlist info (get all video URLs)
                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

                # Check if it's a playlist
                if 'entries' in data:
                    # Playlist
                    for entry in data['entries']:
                        song = entry['url']
                        await play_song(voice_clients[message.guild.id], song)
                else:
                    # Single video
                    song = data['url']
                    await play_song(voice_clients[message.guild.id], song)

            except Exception as e:
                print(f"Error processing message: {e}")

        if message.content.startswith("pause"):
            try:
                voice_clients[message.guild.id].pause()
            except Exception as e:
                print(e)

        if message.content.startswith("-resume"):
            try:
                voice_clients[message.guild.id].resume()
            except Exception as e:
                print(e)

        if message.content.startswith("-stop"):
            try:
                voice_clients[message.guild.id].stop()
                await voice_clients[message.guild.id].disconnect()
            except Exception as e:
                print(e)
        
        if message.content.startswith("?loop"):
            try:
                voice_clients[message.guild.id].loop()
                await voice_clients[message.guild.id].disconnect()
            except Exception as e:
                print(e)
                
    async def play_song(voice_client, song_url):
        """Function to play a song using FFmpeg."""
        player = discord.FFmpegOpusAudio(song_url, **ffmpeg_options)
        
        # Play the song
        voice_client.play(player)
        
        # Wait until the song finishes playing
        while voice_client.is_playing():
            await asyncio.sleep(1)
        
        
    client.run(TOKEN)