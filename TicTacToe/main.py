import discord
from discord.ext import commands



token = 'bot token'

status = "TicTacToe-test"

prefix = "t?"

bot = commands.Bot(prefix)


@bot.event
async def on_ready():
    print("Bot is Ready.")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{status}"))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error


initial_extensions = ['cogs.ttt']

for ext in initial_extensions:
    bot.load_extension(ext)


bot.run(token)
