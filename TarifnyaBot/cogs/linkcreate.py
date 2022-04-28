import discord
from discord_components import *
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

class Lc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Linkcreate : ✅')

    @cog_ext.cog_slash(name="lc",description="csinál egy gombot")
    @commands.has_role('►│🔧 Bot+')
    async def lc(self, ctx, url=None, *, button=None):
        if url == None:
            ctx.send("Írj valami Link-et")
        elif button == None:
            ctx.send("Szöveget is írj a Link mellé")
        else:
            await ctx.channel.send(
                "",
                components=[
                    Button(style=ButtonStyle.URL, label=button, url=url)
                ]
            )
            await ctx.message.delete()



def setup(bot):
    bot.add_cog(Lc(bot))