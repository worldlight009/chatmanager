import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

intents = discord.Intents.all()
bot = Bot(command_prefix="b15?", intents=intents)

@bot.event
async def on_ready():
	print('Hello')

bot.run('TOKEN')