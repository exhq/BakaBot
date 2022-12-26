import time
from discord import Message
from discord.ext.commands import Bot, check, Context
import pathlib
import os


async def checkformessages(message: Message):
    with open('timer') as f:
        lines = f.readlines()
        gamering = int(time.time()) - int(lines[0])
        print(gamering)
        if gamering < 300:
            return

    if "touhou" in message.content:
        await message.reply("https://cdn.discordapp.com/attachments/918571405212270652/1056934396852191343/to_ho.mp4")
        os.system(f"echo {int(time.time())} > timer")
    if "rent" in message.content:
        await message.reply(
        "https://media.discordapp.net/stickers/1009434642123870298.png")
        os.system(f"echo {int(time.time())} > timer")

