import discord
from discord import app_commands
from discord.ext import commands

from config import *


intents = discord.Intents().all()

bot = commands.Bot(command_prefix = "$", description = ".", intents=intents)

intents.messages = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id}) and said : Nah I'd be ready")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=708416606274846803))
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f'Hi {member.name}, Salut mon reuf, bienvenue hn')
 
@bot.tree.command(guild=discord.Object(id=708416606274846803), name="ping", description="Ping pong test !")
async def ping_slash(interation: discord.Interaction):
    await interation.response.send_message("Pong !")

bot.run(tokenNJK)


