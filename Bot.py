#
#
# This is the driver for the Bot, all commands route to pf2.py which does the heavy-lifting. 
# Tokens are not included in the git, for security.
#
#
import discord
from discord.ext import commands
import random
import pf2
import re
import tokens

bot = commands.Bot(command_prefix='!', description='used for DnD')

# Prints to console confirmation that the bot has turned on
@bot.event
async def on_ready():
    print("ON")

# Calls pf2 to print a trait, performs re.sub to remove the command from the message
@bot.command(name="trait", description="Search for a trait\nUsage: !trait {trait_name}, it will find the first trait that matches your term", aliases=['traits', 'tr'])
async def trait(ctx):
    try:
        await ctx.send(pf2.get_trait(strip_command(ctx.message.content)))
    except:
        await ctx.send("Error: Trait not found")

# Calls pf2 to print a condition, performs re.sub to remove the command from the message
@bot.command(name="condition", description="Search for a condition\nUsage: !condition {condition_name}, it will find the first condition that matches your term", aliases=['cond', 'conditions', 'conds'])
async def condition(ctx):
    try:
        await ctx.send(pf2.get_condition(strip_command(ctx.message.content)))
    except:
        await ctx.send("Error, that condition was not found")

# Calls pf2 to print a spell, performs re.sub to remove the command from the message
@bot.command(name="spell", description="Search for a Spell\nUsage: !spell {spell_name}, it will find the first spell that matches your search term", aliases=['spells', 'sp'])
async def spell(ctx):
    try:
        await ctx.send(pf2.get_spell(strip_command(ctx.message.content)))
    except:
        await ctx.send("Error, that spell was not found")

def strip_command(s: str):
    return re.sub(r'!\w* ', '', s);

bot.run(tokens.bot_token)
