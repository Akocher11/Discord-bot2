import datetime
import time
import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


class Otletsay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Otlet : ✅')
        print('Say : ✅')

    @cog_ext.cog_slash(name="otlet",description="ki mondasz vele egy ötletet")
    async def otlet(self, ctx, *, saymsg=None):
        if saymsg == None:
            return await ctx.send("Írj valami ötletet a /otlet után és úgy jó lesz!")
        sayEmbed = discord.Embed(title=f"{ctx.author.name} ötlete :", color=discord.Color.blue(),
                                 description=f"{saymsg}")

        Embed = await ctx.send(embed=sayEmbed)
        await Embed.add_reaction(emoji="✅")
        await Embed.add_reaction(emoji="❌")

    @cog_ext.cog_slash(name="say",description="ki mondasz a bottal valamit")
    @commands.has_role('►│🔧 Bot+')
    async def say(self, ctx, *, saymsg=None):
        if saymsg == None:
            return await ctx.send("Írj valami szöveget a /say után és úgy jó lesz!")
        sayEmbed = discord.Embed(title=f"{ctx.author.name} Mondta :", color=discord.Color.red(),
                                 description=f"{saymsg}")

        await ctx.send(embed=sayEmbed)

def setup(bot):
    bot.add_cog(Otletsay(bot))