import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Unban : ✅')

    @cog_ext.cog_slash(name="unban",description="unbannol egy embert")
    @commands.has_role('►│🔧 Bot+')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await  ctx.send(f'{ctx.author.mention} feloldotta {user.mention} banját')
                return

def setup(bot):
    bot.add_cog(Unban(bot))