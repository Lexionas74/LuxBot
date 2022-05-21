import nextcord
from nextcord.ext import commands
import os
from datetime import datetime
from nextcord import Guild, Interaction, Message
from nextcord.ext import commands

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

@bot.slash_command()
async def ping(self, ctx):
	ping = nextcord.Embed(title="Bot latency", description=f"`{round(self.bot.latency * 1000)}ms`", color=nextcord.Colour.green())
	ping.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.display_avatar.url)    
	await ctx.send(embed=ping) 
  
bot.run(my_secret)
