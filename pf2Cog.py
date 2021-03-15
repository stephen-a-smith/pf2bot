import discord
from discord.ext import commands
import pf2

class pf2Cog(commands.Cog, name="Pathfinder"):
  """
  This is a subset of commands for Pathfinder.
  """
  def __init__(self, bot):
    self.bot = bot

  # Calls pf2 to print a trait
  @commands.command(name="trait", aliases=['traits', 'tr'])
  async def trait(self, ctx, s: str):
      '''
      Search for a trait
      
      Usage: !trait {trait_name}, it will find the first trait that matches your term
      '''
      try:
          await ctx.send(pf2.get_trait(s))
      except:
          await ctx.send("Error: Trait not found")

  # Calls pf2 to print a condition
  @commands.command(name="condition", aliases=['cond', 'conditions', 'conds'])
  async def condition(self, ctx, s: str):
      """
      Search for a condition
      
      Usage: !condition {condition_name}, it will find the first condition that matches your term
      """
      try:
          await ctx.send(pf2.get_condition(s))
      except:
          await ctx.send("Error, that condition was not found")

  # Calls pf2 to print a spell
  @commands.command(name="spell", aliases=['spells', 'sp'])
  async def spell(self, ctx, s: str):
      """
      Search for a Spell
      
      Usage: !spell {spell_name}, it will find the first spell that matches your search term
      """
      try:
          await ctx.send(pf2.get_spell(s))
      except:
          await ctx.send("Error, that spell was not found")

def setup(bot):
    bot.add_cog(pf2Cog(bot))