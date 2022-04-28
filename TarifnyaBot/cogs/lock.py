import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Lock : ✅')

    @cog_ext.cog_slash(name="lock",description="Lezár egy szobát")
    @commands.has_role('►│🔧 Bot+')
    async def lock(self, ctx):
        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(title=f"🔒 Locked by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Lock(bot))