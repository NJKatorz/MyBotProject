import discord
from discord.ext import commands
""" Token = NzQ5MTk0NjQxNTY3MzgzNjEz.G4HiNH.8NM6HE86xcx7SSg-tCw-KAvu2xTlNWcBfRMM20 """

bot = commands.Bot(command_prefix = "$", description = ".")

@bot.event
async def on_ready():
	print("I'm ready !")

@bot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f'Hi {member.name}, Salut mon reuf, bienvenue hn')

@bot.command()
async def yo(ctx):
	await ctx.send("Yo la miff bien ou bien ")

@bot.command()
async def ol(ctx):
	await ctx.send("SHINEEEE!!!")

@bot.command()
async def hey():
	await bot.say("Hello world")

bot.run("NzQ5MTk0NjQxNTY3MzgzNjEz.G4HiNH.8NM6HE86xcx7SSg-tCw-KAvu2xTlNWcBfRMM20")
