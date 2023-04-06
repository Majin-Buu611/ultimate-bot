import os
import discord
from discord.ext import commands, tasks
from command_modules.Utils import Utils

intents = discord.Intents.all();
bot = commands.Bot(command_prefix = ".", intents = intents)
client = discord.Client(intents = intents);

@bot.event
async def on_ready():
  print("I'm ready!")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        return
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Missing argument.")
    else:
        await ctx.send(f"An error occurred: {error}")

async def setup_hook(bot):
  for filename in os.listdir('./command_modules'):
    if filename.endswith('.py'):
      await bot.load_extension(f'command_modules.{filename[:-3]}')

token_env = os.environ["DISCORD_BOT_TOKEN"]
bot.run(token_env)