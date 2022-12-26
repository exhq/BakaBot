import io
import random
from urllib.request import urlopen

import discord
import xmltodict
from PIL import Image, ImageOps, ImageDraw, ImageFont
from discord import Message, Attachment
from discord.ext.commands import Bot, check, Context

import alias as aliases
import gamering
from checkformessages import checkformessages

adminperms = [712639419785412668, 268103439614083074,
              867751309923188737, 369197839680536576, 198407032200626176]
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
    if not context.message.attachments:
        return
    attachment: Attachment = context.message.attachments[0]
    input_file = io.BytesIO()
    await attachment.save(input_file)
    input_file.seek(0)
    image = Image.open(input_file)

    color = "white"
    border = (0, 150, 0, 0)
    image = ImageOps.expand(image, border=border, fill=color)

    dr = ImageDraw.Draw(image)
    ft = ImageFont.truetype('/usr/share/fonts/TTF/Impact.TTF', 70)

    _, _, text_width, text_height = dr.textbbox((0, 0), text, font=ft)
    dr.text(((image.width - text_width) / 2, 50), text, font=ft, fill=(0, 0, 0))

    output_file = io.BytesIO()
    image.save(output_file, format="png")
    output_file.seek(0)
    await context.send(file=discord.File(output_file, filename="caption.png"))


@client.group(pass_context=True, invoke_without_command=True)
@dev_only
async def dev(context: Context):
    await context.send("Unknown dev command")


@client.command(pass_context=True, invoke_without_command=True)
async def cute(context: Context):
    lol = []
    choice = context.message.content.split(" ")[1]
    print(choice)
    url = "https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=100&pid=0&tags=" + choice
    response = urlopen(url)
    o = xmltodict.parse(response.read())
    for i in o["posts"]["post"]:
        try:
            lol.append(i["@sample_url"])
        except:
            continue

    if not len(lol) == 0:
        await context.send(random.choice(lol))
    else:
        await context.send("couldnt find anything")


@dev.command(pass_context=True)
@dev_only
async def kill(context: Context):
    await context.send("The IRS is gonna get me one day.")
    await client.close()
    exit()


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
        await message.channel.send(f"Unknown alias {alias}")


aliases.load()
client.add_command(gamering.rps)
client.run(TOKEN.read())
