import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help : ✅')

    @cog_ext.cog_slash(name="help",description="ki írja a parancsokat")
    async def help(self, ctx, command_name=None):
        if command_name == None:
            em = discord.Embed(title='Help',
                           description="Használd a /help <parancs>-ot hogy tudd meg hogyan kell használni")

            em.add_field(name="__Ember moderáció__", value="kick\nban\nunban\nmute\nunmute")
            em.add_field(name="__Chat moderáció__", value="lock\nunlock\nnuke\nabw\nrbw")
            em.add_field(name="__Chat__", value="otlet -\nsay")
            em.add_field(name="__Fun__", value="tictactoe -\n(place) -\nrandomg -")
            em.add_field(name="__Button__", value="lc")
            em.add_field(name="__+__", value="gstart")

            await ctx.send(embed=em)
        elif command_name == "SayEmbed":
            em = discord.Embed(title="__SayEmbed__", description="Ki rúgja a meg pingelt embert")
            em.add_field(name="**Használata**", value="/kick @ember <indok>")

            await ctx.send(embed=em)

        elif command_name == "kick":
            em = discord.Embed(title="__Kick__", description="Ki rúgja a meg pingelt embert")
            em.add_field(name="**Használata**", value="/kick @ember <indok>")

            await ctx.send(embed=em)

        elif command_name == "ban":
            em = discord.Embed(title="__Ban__", description="Ki bannolja a meg pingelt embert")
            em.add_field(name="**Használata**", value="/ban @ember <indok>")

            await ctx.send(embed=em)

        elif command_name == "unban":
            em = discord.Embed(title="__Unban__", description="Unbannolja az adott embert")
            em.add_field(name="**Használata**", value="/unban Akocher11#7376")

            await ctx.send(embed=em)

        elif command_name == "mute":
            em = discord.Embed(title="__Mute__", description="Mute-olja a meg pingelt embert")
            em.add_field(name="**Használata**", value="/mute @ember <indok>")

            await ctx.send(embed=em)

        elif command_name == "unmute":
            em = discord.Embed(title="__Unmute__", description="Unmute-olja a meg pingelt embert")
            em.add_field(name="**Használata**", value="/unmute @ember")

            await ctx.send(embed=em)

        elif command_name == "lock":
            em = discord.Embed(title="__Lock__", description="Lezárja azt a csatornát amelyikbe beírtad a lockot")
            em.add_field(name="**Használata**", value="/lock")

            await ctx.send(embed=em)

        elif command_name == "unlock":
            em = discord.Embed(title="__Unlock__",
                               description="Lezárásból feloldja azt a csatornát amelyikbe beírtad az unlockot")
            em.add_field(name="**Használata**", value="/unlock")

            await ctx.send(embed=em)

        elif command_name == "nuke":
            em = discord.Embed(title="__Nuke__",
                               description="Törli az üzenet előzményeket(Ha nem írsz be számot akkor az összeset"
                                           "törli)")
            em.add_field(name="**Használata**", value="/nuke <szám>")

            await ctx.send(embed=em)

        elif command_name == "abw":
            em = discord.Embed(title="__abw__",
                               description="(AddBannedWord), ha valaki beírja a tiltott szót akkor automatikusan törli")
            em.add_field(name="**Használata**", value="/abw <tiltó szó>")

            await ctx.send(embed=em)

        elif command_name == "rbw":
            em = discord.Embed(title="__rbw__", description="(RemoveBannedWord), törli a tiltó listáról a szót")
            em.add_field(name="**Használata**", value="/rbw <tiltott szó>")

            await ctx.send(embed=em)

        elif command_name == "otlet":
            em = discord.Embed(title="__Otlet__", description="ki írsz vele egy ötletet")
            em.add_field(name="**Használata**", value="/otlet <ötleted>")

            await ctx.send(embed=em)

        elif command_name == "say":
            em = discord.Embed(title="__Say__", description="ki íratod a bottal a amit szeretnél mondani")
            em.add_field(name="**Használata**", value="/say <Mondani valód>")

            await ctx.send(embed=em)
        elif command_name == "tictactoe":
            em = discord.Embed(title="__TicTacToe__", description="3x3-as Amőba Fun game")
            em.add_field(name="**Használata**", value="/tictactoe <@Játékos> <@Játékos2>")

            await ctx.send(embed=em)

        elif command_name == "place":
            em = discord.Embed(title="__TicTacToe__",
                               description="Ha elindult egy tictactoe játék ezzel tudsz helyezni.")
            em.add_field(name="**Használata**", value="/place <szám>")

            await ctx.send(embed=em)

        elif command_name == "gstart":
            em = discord.Embed(title="__Giveaway__", description="indít egy giveawayt")
            em.add_field(name="**Használata**", value="/gstart (a továbbiakat ki írja)")

            await ctx.send(embed=em)


        elif command_name == "randomg":
            em = discord.Embed(title="__Randomg__", description="Generál két szám között egy random számot")
            em.add_field(name="**Használata**", value="/randomg <szám1> <szám2>")

            await ctx.send(embed=em)

        elif command_name == "lc":
            em = discord.Embed(title="__LinkCreate__", description="Csinál egy gombot")
            em.add_field(name="**Használata**", value="/lc <link ahova dobjon ha rányomsz> <gomb tartalma>")

            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Help(bot))