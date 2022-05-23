import nextcord
from nextcord.ext import commands
import os
from datetime import datetime
from nextcord import Guild, Interaction, Message
from nextcord.ext import commands
import aiohttp
import asyncio

bot = commands.Bot(command_prefix="s!", intents=nextcord.Intents.all(), owner_ids ={935434855397871628, 687882857171255309})
my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
	print("3")
	print("2")
	print("1")
	print("Blastoff!") # Space theme lol

@bot.command()
async def test(ctx):
	await ctx.send("Test completed")
	
@bot.slash_command(name="hi", description="This is a test")
async def hi(interaction: Interaction):
	await interaction.response.send_message("HI")
	
@bot.slash_command(name="about", description="About the bot")
async def about(interaction: Interaction):
	embed = nextcord.Embed(title="About", description="LuxBot is a bot created by Lexionas#1535 and Luziaf#9464 for an event!\nHope you enjoy the bot!", color=nextcord.Colour.green())
	await interaction.response.send_message(embed=embed)

@bot.slash_command(name="ping", description="See the latency of the bot")
async def ping(interaction: Interaction):
	ping = nextcord.Embed(title="Bot latency", description=f"`{round(bot.latency * 1000)}ms`", color=nextcord.Colour.green()) 
	await interaction.response.send_message(embed=ping)

@bot.slash_command(name="ban", description="Ban a member from the server")
async def ban_member(interaction: Interaction, member: nextcord.Member, reason="No reason provided"):
  await member.ban(reason=reason)
  await interaction.response.send_message(f"{member} has been banned from the spaceship\nReason : {reason}")

@bot.slash_command(name="kick", description="Kick a member from the server")
async def kick_member(interaction: Interaction, member : nextcord.Member, reason="No reason provided"):
	await member.kick(reason=reason)
	await interaction.response.send_message(f"{member} was ejected from the spaceship\nReason : {reason}")
  
bot.run(my_secret)
