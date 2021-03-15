import discord
from discord.ext import commands
import pf2
import traceback

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
      If searching a term with spaces, wrap them in quotes to ensure it finds the right term
      '''
      try:
          await ctx.send("```" + pf2.get(s, pf2.traits) + "```")
      except:
          await ctx.send("Error: Trait not found, good luck finding it in the book lmao")

  # Calls pf2 to print a condition
  @commands.command(name="condition", aliases=['cond', 'conditions', 'conds'])
  async def condition(self, ctx, s: str):
      """
      Search for a condition
      
      Usage: !condition {condition_name}, it will find the first condition that matches your term
      If searching a term with spaces, wrap them in quotes to ensure it finds the right term
      """
      try:
          await ctx.send("```"  + pf2.get(s, pf2.conds) + "```")
      except:
          await ctx.send("Error, that condition was not found, check page 618 in the book.")

  # Calls pf2 to print a spell
  @commands.command(name="spell", aliases=['spells', 'sp'])
  async def spell(self, ctx, s: str):
      """
      Search for a Spell
      
      Usage: !spell {spell_name}, it will find the first spell that matches your search term
      If searching a term with spaces, wrap them in quotes to ensure it finds the right term
      """
      try:
          await ctx.send("```" + pf2.get(s, pf2.spells) + "```")
      except:
          await ctx.send("Error, that spell was not found, check page 316 in the book.")

  # Calls pf2 to print a Feat
  @commands.command(name="feat", aliases=['feats'])
  async def feat(self, ctx, s: str):
      """
      Search for a Feat
      
      Usage: !feat {feat_name}, it will find the first feat that matches your search term
      If searching a term with spaces, wrap them in quotes to ensure it finds the right term
      """
      try:
          await ctx.send("```" + pf2.get(s, pf2.feats) + "```")
      except:
          await ctx.send("Error, that feat was not found, good luck finding it in the book lmao")

def setup(bot):
    bot.add_cog(pf2Cog(bot))