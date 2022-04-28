import random
import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


class Randomg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Randomg : ✅")

    @cog_ext.cog_slash(name="randomg",description="sorsol egy számot a két meg adott szám között")
    async def randomg(self, ctx, num1 = None, num2 = None):
        if num1 == None:
            await ctx.send("Írj két számot pl.: ?randomg 10 30")
        elif num2 == None:
            await ctx.send("Írj két számot pl.: ?randomg 10 30")
        else:
            num = random.randint(int(num1), int(num2))
            await ctx.send(f'A kapott szám az a : {num}')




def setup(bot):
    bot.add_cog(Randomg(bot))