import nextcord
from nextcord.ext import commands
import os
import urllib
import json
from datetime import datetime
from nextcord import Guild, Interaction, Message
from nextcord.ext import commands
import aiohttp
import asyncio
import random

bot = commands.Bot(command_prefix="s!", intents=nextcord.Intents.all(), owner_ids ={935434855397871628, 687882857171255309},  help_command=None, )
my_secret = os.environ['TOKEN']
NASA = os.environ['NASAKEY']

@bot.event
async def on_ready():
	print("3")
	print("2")
	print("1")
	print("Blastoff!") # Space theme lol
	await ch_pr()

	
@bot.slash_command(name="about", description="About the bot") #this command shows a small bit of info about the bot
async def about(interaction: Interaction):
	embed = nextcord.Embed(title="About", description="LuxBot is a bot created by Lexionas#1535 and Luziaf#9464 for an event!\nHope you enjoy the bot!", color=nextcord.Colour.green())
	await interaction.response.send_message(embed=embed)

@bot.slash_command(name="ping", description="See the latency of the bot") #this command shows the bots ping
async def ping(interaction: Interaction):
	ping = nextcord.Embed(title="Bot latency", description=f"`{round(bot.latency * 1000)}ms`", color=nextcord.Colour.green()) 
	await interaction.response.send_message(embed=ping)

@bot.slash_command(name="ban", description="Ban a member from the server") #this command bans a member from the server
async def ban_member(interaction: Interaction, member: nextcord.Member, reason="No reason provided"):
  await member.ban(reason=reason)
  await interaction.response.send_message(f"{member} has been exiled from the spaceship\nReason : {reason}")

@bot.slash_command(name="kick", description="Kick a member from the server") #this command kicks a member from the server
async def kick_member(interaction: Interaction, member : nextcord.Member, reason="No reason provided"):
	await member.kick(reason=reason)
	await interaction.response.send_message(f"{member} was ejected from the spaceship\nReason : {reason}")

@bot.slash_command(name="unban", description="Bring a member back from exile") #this command unbans a user from the server
async def unban(interaction: Interaction, user : nextcord.User):
	await interaction.guild.unban(user=user)
	await interaction.response.send_message(f"{user} was unexiled")

@bot.slash_command(name="apod", description="Astronomy Pictures of the Day (Updates Daily)") #this command sends a astrology picture, one that updates every day!
async def apod(interaction: Interaction):
  api = urllib.request.urlopen(f'https://api.nasa.gov/planetary/apod?api_key={NASA}')
  data = json.load(api)
  explanation = data['explanation']
  image = data['url']
  date = data['date']
	
  embed = nextcord.Embed(title="Astronomy Picture of the Day", description=explanation, color=nextcord.Colour.green())
  embed.set_image(url=image)
  embed.set_footer(text=f"Image and Explanation fron NASA. ({date})")
  
  await interaction.response.send_message(embed=embed)

async def ch_pr(): #changes the status, all space related :)
    await bot.wait_until_ready()
    statuses = ["the stars", "Andromeda travel towards us", "Earth burn", "the space time continuum", "the universe expand"]
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=nextcord.Activity(
            type=nextcord.ActivityType.watching, name=status))
        await asyncio.sleep(300) 

bot.run(my_secret)
