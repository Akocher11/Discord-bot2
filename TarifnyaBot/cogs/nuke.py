import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Nuke : ✅')

    @cog_ext.cog_slash(name="nuke",description="ki törli az üzenet előzményeket.")
    @commands.has_role('►│🔧 Bot+')
    async def nuke(self, ctx, amount=10000):
        await ctx.channel.purge(limit=int(amount))
        embed = discord.Embed(title='', Color=0xff087f)
        embed.add_field(name=f'Nuked by {ctx.author.name}',
                        value='ennek a szobának az üzenetei törölve!')
        await ctx.channel.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Nuke(bot))