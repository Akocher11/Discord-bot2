import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mute : ✅')

    @cog_ext.cog_slash(name="mute",description="Mute-ol egy embert")
    @commands.has_role('►│🔧 Bot+')
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name='Muted') #►│👤 Tag
        TagRole = discord.utils.get(guild.roles, name='►│👤 Tag')

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False,
                                              read_messages=False)

            await member.add_roles(mutedRole, reason=reason)
            await member.remove_roles(TagRole)
            await ctx.send(f'Muted {member.mention} azért mert {reason}')
            await member.send(f'Le lettél némítva Tarifnya szerverén mert {reason}')
        else:
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=True)
            await member.add_roles(mutedRole, reason=reason)
            await member.remove_roles(TagRole)
            await ctx.send(f'Muted {member.mention} azért mert {reason}')
            await member.send(f'Le lettél némítva a Tarifnya szerverén mert {reason}')


def setup(bot):
    bot.add_cog(Mute(bot))
