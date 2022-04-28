import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Kick : ✅')

    @cog_ext.cog_slash(name="kick",description="ki kickel egy embert")
    @commands.has_role('►│🔧 Bot+')
    async def kick(self, cty, member: discord.Member, *, reason=None):
        if member == None:
            await cty.send("Írj embert indokkal együtt. /kick @ember spamelt")
        else:
            await member.kick(reason=reason)
            await cty.send(f'Kicked {member.mention} by {cty.author.mention}')


def setup(bot):
    bot.add_cog(Kick(bot))