import discord
from discord.ext import commands
import random
import daytime

class Utils(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def randnum(self, ctx, minRange: int = 0, maxRange: int = 9999, inclusiveMin: bool = True, inclusiveMax: bool = True):
    if not inclusiveMin:
      minRange += 1
    if not inclusiveMax:
      maxRange -= 1
    await ctx.send(random.randint(minRange, maxRange))

