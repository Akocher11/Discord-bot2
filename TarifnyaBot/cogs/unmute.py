import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Unmute : ✅\n\n--------------------------------------------\n')

    @cog_ext.cog_slash(name="unmute",description="unmute-ol egy embert")
    @commands.has_role('►│🔧 Bot+')
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name='Muted')

        await member.remove_roles(mutedRole)
        await ctx.send(f'Unmuted {member.metion}')
        await member.send('Unmuteolva lettél Tarifnya szerverén Irány chatelni')


def setup(bot):
    bot.add_cog(Unmute(bot))