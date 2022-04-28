import discord
from discord.ext import commands
import random
import asyncio
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import json
import os
import re

if os.path.exists(os.getcwd() + "/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"bannedWords": []}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)



token = "" #tokenedet rakd be
bannedWords = configData["bannedWords"]

bot = commands.Bot(command_prefix='/')
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command("help")

@bot.event  # Bot elindító
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="/help / Prefix : /"))
    print(f"\n\n\nBot logged in as {bot.user}\n\n-------------------------------------------------\n\nGstart : ✅\nTTT : ✅")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@slash.slash(name="abw",description="Tiltó listához hozzá adod a szót")
@commands.has_role("►│🔧 Bot+")
async def abw(ctx, szo):
    if szo.lower() in bannedWords:
        await ctx.send("Már ki van bannolva a szó")
    else:
        bannedWords.append(szo.lower())

        with open("./config.json", "r+") as f:
            data = json.load(f)
            data["bannedWords"] = bannedWords
            f.seek(0)
            f.write(json.dumps(data))
            f.truncate()

        await ctx.send("A szó hozzá lett a adva a szó listához")


@slash.slash(name="rbw",description="Tiltó listáról leveszi a bannolt a szót")
@commands.has_role("►│🔧 Bot+")
async def rbw(ctx, bannedszo):
    if bannedszo.lower() in bannedWords:
        bannedWords.remove(bannedszo.lower())

        with open("./config.json", "r+") as f:
            data = json.load(f)
            data["bannedWords"] = bannedWords
            f.seek(0)
            f.write(json.dumps(data))
            f.truncate()

        await ctx.send("A szó törölve lett a tiltó listáról.")
    else:
        await ctx.send("A szó nincs meg tiltva.")


def msg_contains_word(msg, word):
    return re.search(fr'\b({word})\b', msg) is not None


@bot.event
async def on_message(message):
    messageAuthor = message.author

    if bannedWords != None and (isinstance(message.channel, discord.channel.DMChannel) == False):
        for bannedWord in bannedWords:
            if msg_contains_word(message.content.lower(), bannedWord):
                await message.delete()
                await message.channel.send(
                    f"{messageAuthor.mention} az üzeneted törölve lett ne beszélj csúnyán")

    await bot.process_commands(message)

def convert(time):
    pos = ["s", "m", "h", "d", "w"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24, "w": 3600 * 24 * 7}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@slash.slash(name="gstart",description="elindít egy giveawayt")
@commands.has_role('►│🔧 Bot+')
async def gstart(ctx):
    timeout = 30.0
    embedq1 = discord.Embed(title=":tada: | SETUP GIVEAWAY",
                            description=f"Ennyi másodperced van az írásig ``{timeout}`` Siess!", color=ctx.author.color)
    embedq1.add_field(name=":star: | Elsö lépes",
                      value="Melyik csatornába legyen a giveaway?\n\n **Példul**: ``#General``")
    embedq2 = discord.Embed(title=":tada: | SETUP GIVEAWAY", description="Remek! Térjünk a következő kérdésre.",
                            color=ctx.author.color)
    embedq2.add_field(name=":star: | Második lépés",
                      value="Milyen hosszú legyen a Giveaway? ``<s|m|h|d|w>``\n\n **Például**:\n ``1d``")
    embedq3 = discord.Embed(title=":tada: | SETUP GIVEAWAY", description="Ragyogó. Eljutottál az utolsó kérdésig!",
                            color=ctx.author.color)
    embedq3.add_field(name=":star: | Utolsó lépés", value="Mit lehet nyerni?\n\n **Például**:\n ``NITRO``")

    questions = [embedq1,
                 embedq2,
                 embedq3]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(embed=i)

        try:
            msg = await bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            embed = discord.Embed(title=":tada: **Giveaway SETUP**", description=":x: Túl lassú voltál, próbáld újra",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2: -1])
    except:
        embed = discord.Embed(title=":tada: **Giveaway SETUP**", description=":x: Nem jól adtad meg a csatornát!",
                              color=discord.Color.red())
        await ctx.send(embed=embed)
        return

    channel = bot.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        embed = discord.Embed(title=":tada: **Giveaway SETUP**",
                              description=":x: Nem használt megfelelő időegységet, itt egy lista:\n> s = másodperc\n> m = perc\n> h = óra\n> d = nap\n> w = hét!",
                              color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    elif time == -2:
        embed = discord.Embed(title=":tada: **Giveaway SETUP**",
                              description=":x: Az időnek **EGÉSZ** számnak kell lennie", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    prize = answers[2]

    embed = discord.Embed(title=":tada: **Giveaway SETUP**",
                          description="OKÉ, minden korrekt volt. A Giveaway most kezdődik!",
                          color=discord.Color.green())
    embed.add_field(name="Giveaway csatornája", value=f"{channel.mention}")
    embed.add_field(name="Idő:", value=f"{answers[1]}")
    embed.add_field(name="Nyeremény:", value=prize)
    await ctx.send(embed=embed)
    print(
        f"Új verseny indul: {ctx.author.mention} | Ebben a csatornában: {channel.mention} | Idő: {answers[1]} | Nyeremény : {prize}")
    print("------")
    embed = discord.Embed(title=f":tada: **Ez lesz kisorsolva : {prize}**",
                          description=f"Reagálj az üzenetre hogy tudj csatlakozni : 🎉 ", color=0x32cd32)
    embed.add_field(name="Idő:", value=answers[1])
    embed.add_field(name=f"Elindította :", value=ctx.author.mention)
    msg = await channel.send(embed=embed)

    await msg.add_reaction('🎉')
    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(msg.id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)
    if True == True:
        await channel.send(f":tada: Gratulálunk {winner.mention} nyerte a Giveawayt, Ezt nyerte : **{prize}**!")
        print(f"Új nyertes! Ő pedig nem más mint : {winner.mention} | Ezt nyerte : {prize}")
        print("------")

    embed2 = discord.Embed(title=f":tada: **Ezt lehetett nyerni: {prize}**",
                           description=f":trophy: **Nyertes:** {winner.mention}", color=0xffd700)
    embed2.set_footer(text="A giveaway véget ért")
    await msg.edit(embed=embed2)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


@slash.slash(name="tictactoe",description="El indít egy TicTacToe játékot")
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send(f"{p1} jön")
        elif num == 2:
            turn = player2
            await ctx.send(f"{p2} jön")
    else:
        await ctx.send("Éppen egy játékban vagy játszd le az előzőt, hogy kezdhess újat!")


@slash.slash(name="place",description="A tictactoe játékban ezzel tudsz helyezni (pos hoz számot írj)")
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " nyert!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Döntetlen lett")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("csak 1-9 lévő számot írhatsz be ami persze üres.")
        else:
            await ctx.send("Most nem te jössz.")
    else:
        await ctx.send("Elősször indíts egy játékot ?tictactoe @player @player")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("2. személyt is kell írnod a játékhoz")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Légyszi jelöld meg a személyt ne csak leírd a nevét.")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Írj számot is ahova szeretnéd rakni")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("csak számot írj.")

@slash.slash(name="roomsay", description="Küld egy üzenetet a meg adott csatornába.")
async def csay(ctx, room, *, message):
    gen = int(room[2: -1])
    channel = bot.get_channel(gen)
    await channel.send(message)

@slash.slash(name="SayEmbed", description="Küld egy Embed üzenetet a meg adott csatornába.")
async def SayEmbed(ctx, uzenet_cim, uzenet_tartalma, csatorna_neve):
    Embed = discord.Embed(title=uzenet_cim, description=uzenet_tartalma)
    id = int(csatorna_neve[2: -1])
    channel = bot.get_channel(id)
    await channel.send(embed=Embed)

bot.run(token)