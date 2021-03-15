#
#
# This is the driver for the Bot, all commands route to pf2.py which does the heavy-lifting. 
# Tokens are not included in the git, for security.
#
#
import discord
from discord.ext import commands
import tokens

bot = commands.Bot(command_prefix='!', description='A simple bot for PF2')

# Prints to console confirmation that the bot has turned on
@bot.event
async def on_ready():
    print("ON")

bot.load_extension('pf2Cog')
bot.run(tokens.bot_token)
