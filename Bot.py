import discord
from discord.ext import commands
import random
import pf2
import re
import tokens

bot = commands.Bot(command_prefix='!', description='used for DnD')

@bot.event
async def on_ready():
    print("ON")

@bot.command(name="trait", description="Search for a trait\nUsage: !trait {trait_name}, it will find the first trait that matches your term")
async def trait(ctx):
    try:
        await ctx.send(pf2.get_trait(re.sub(r'!trait ', '', ctx.message.content)))
    except:
        await ctx.send("Error: Trait not found")

@bot.command(name="condition", description="Search for a condition\nUsage: !condition {condition_name}, it will find the first condition that matches your term")
async def condition(ctx):
    try:
        await ctx.send(pf2.get_condition(re.sub(r'!condition ', '', ctx.message.content)))
    except:
        await ctx.send("Error, that condition was not found")

@bot.command(name="spell", description="Search for a Spell\nUsage: !spell {spell_name}, it will find the first spell that matches your search term")
async def spell(ctx):
    try:
        await ctx.send(pf2.get_spell(re.sub(r'!spell ', '', ctx.message.content)))
    except:
        await ctx.send("Error, that spell was not found")

bot.run(tokens.bot_token)
