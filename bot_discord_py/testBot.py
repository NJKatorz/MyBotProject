from ast import Delete
from turtle import filling
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "My bot")

@bot.event
async def on_ready ():
	print("I'm ready bro !")
	 
@bot.command()
async def coucou(ctx):
	await ctx.send("Coucou !")

@bot.command()
async def ui(ctx):
	await ctx.send("Ui")
	

@bot.command()
async def photo(ctx):
	await ctx.send(file=discord.File('images\Myhero.jpg'))

@bot.command()
async def say(ctx, *texte):
	await ctx.send(" ".join(texte))

@bot.command()
async def clearr(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()

@bot.command()
async def sort(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} a été expulsé(e) du serveur. Salut hn :).")

@bot.command()
async def degage(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} a été ban du serveur : {reason}.")

token = "NzI0NTMyNjIyMjg1NjAyODg4.XvBm6Q.CUr583m_Dxoo_LRN2Jxor5Li6rc"

bot.run(token)

