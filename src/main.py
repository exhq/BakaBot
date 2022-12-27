
import random
from urllib.request import urlopen
import etc
import discord
import xmltodict
from discord import Message
from discord.ext.commands import Bot, check, Context
import pathlib
import alias as aliases
import gamering
from checkformessages import checkformessages

adminperms = [712639419785412668, 268103439614083074,
              867751309923188737, 369197839680536576, 198407032200626176, 266994249344614410]
TOKEN = open("../TOKEN", "r")


@check
def dev_only(context: Context):
    return context.author.id in adminperms


intents = discord.Intents.default()
intents.message_content = True

client = Bot(intents=intents, command_prefix="!")


@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')


@client.command(pass_context=True)
async def caption(context: Context, *, text: str):
    await context.reply("temporary out of order.")


@client.group(pass_context=True, invoke_without_command=True)
@dev_only
async def dev(context: Context):
    await context.send("Unknown dev command")



@client.command(pass_context=True, invoke_without_command=True)
async def howretard(context: Context, *, lmao: discord.Member):
    random.seed(str(lmao))
    test = random.randint(1,100)
    checknick = ""
    if lmao.nick == None:
        checknick = lmao.name
    else:
        checknick = lmao.nick
    await context.reply(f"{checknick} is {test}% retarded")

@client.command(pass_context=True, invoke_without_command=True)
async def cute(context: Context):
    blacklist = pathlib.Path('block')
    a = blacklist.read_text()
    print(a)
    among = []
    uop = context.message.content.split(" ")[1]
    print(uop, "bleh")
    url = "https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=100&pid=0&tags=" + uop
    print(uop)
    response = urlopen(url)
    o = xmltodict.parse(response.read())
    for i in o["posts"]["post"]:
        try:
            among.append(i["@sample_url"])
        except:
            continue

    if not len(among) == 0:
        await context.send(random.choice(among))
    else:
        await context.send("couldnt find anything")


@client.command(pass_context=True, invoke_without_command=True)
async def wot(context: Context):
        await context.send\
("""```
BakaBot2 version idk
prefix: !
cute <name of character>: returns a random picture of the character
howretard <ping>:         proves that we're all retarded
rps <word>                play rps with this bitch
... <alias name>:         can you find them? 

other notable features:
- autorespond - your messages have a chance of being replied by BakaBot
-------------------------------------------------------------------
    
    
thats it for now, please ping me if you have any interesting ideas :)
-ECHO 
ping everythingonarm now, I forked the bot lol
```""")


@dev.command(pass_context=True)
@dev_only
async def kill(context: Context):
    await context.send("The IRS is gonna get me one day.")
    await client.close()
    exit()


@dev.command(pass_context=True)
@dev_only
async def setactivity(context: Context, *, newactivity: str):
    activity = discord.Game(name=newactivity, type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    await context.send("changed activity to " + newactivity)

@dev.command(pass_context=True)
@dev_only
async def qblock(context: Context):
    await etc.qblock(context)



@dev.command(pass_context=True)
@dev_only
async def echo(context: Context, *, rest: str):
    await context.send(rest)


@dev.command(pass_context=True)
@dev_only
async def alias(context: Context, short: str, *, long: str):
    aliases.set_alias(short, long)
    aliases.save()
    await context.send(f"Alias saved:\n{long}")


@client.event
async def on_message(message: Message):
    await checkformessages(message)
    await client.process_commands(message)
    if message.author.bot:
        return
    content = message.content
    if not content.startswith("..."):
        return
    alias = content[3:].strip()
    longform = aliases.get_alias(alias)
    if longform:
        await message.channel.send(longform)
    else:
        await message.reply("Unknown alias")


aliases.load()
client.add_command(gamering.rps)
client.run(TOKEN.read())
