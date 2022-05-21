import nextcord
from nextcord.ext import commands
import os
from datetime import datetime
from nextcord import Guild, Interaction, Message
from nextcord.ext import commands

bot = commands.Bot(command_prefix="s!")
my_secret = os.environ['TOKEN']

@bot.event
async def on_ready():
	print("Blastoff!") # Space theme lol

@bot.command()
async def test(ctx):
	await ctx.send("Test completed")

  
bot.run('TOKEN')
