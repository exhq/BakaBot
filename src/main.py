import random
import urllib
from pprint import pprint

import discord
from discord import Message
from discord.ext.commands import Bot, check, Context
import requests
from urllib.request import urlopen
import xmltodict, json
import os
import alias as aliases
from PIL import Image, ImageOps, ImageDraw, ImageFont
import gamering

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
async def caption(context: Context):
    if context.message.attachments:
        inp = str(context.message.attachments[0])
        filename = inp[inp.rfind("/"):]
        extention = inp[inp.rfind("."):]
        os.system(f"mkdir -p temp; cd temp; wget {inp}; mv ./{filename} input{extention}; cd ..; ")
        print()
        img = Image.open(f"{os.getcwd()}/temp/input{extention}")
        color = "white"
        border = (0, 150, 0, 0)
        new_img = ImageOps.expand(img, border=border, fill=color)
        new_img.save(f"{os.getcwd()}/temp/out.png")

        im = Image.open(f"{os.getcwd()}/temp/out.png")
        W, H = im.size
        dr = ImageDraw.Draw(im)
        ft = ImageFont.truetype('/usr/share/fonts/TTF/Impact.TTF', 70)

        text = " ".join(context.message.content.split(" ")[1:])
        _, _, w, h = dr.textbbox((0, 0), text, font=ft)
        dr.text(((W - w) / 2, 50), text, font=ft, fill=(0,0,0))
        im.save(f"{os.getcwd()}/temp/out.png")
        await context.send(file=discord.File(f"{os.getcwd()}/temp/out.png"))


@client.group(pass_context=True, invoke_without_command=True)
@dev_only
async def dev(context: Context):
    await context.send("Unknown dev command")


@client.command(pass_context=True, invoke_without_command=True)
async def r34(context: Context):
    lol = []
    choice = context.message.content.split(" ")[1]
    print(choice)
    url = "https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=100&pid=0&tags="+choice
    response = urlopen(url)
    o = xmltodict.parse(response.read())
    for i in o["posts"]["post"]:
        lol.append(i["@sample_url"])

    if not len(lol) == 0:
        await context.send(random.choice(lol))
    else:
        await context.send("couldnt find anything")


    # get the result code and print it





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