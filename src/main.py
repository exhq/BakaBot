import discord
from commandprovider import commandprovider
import os
from time import sleep
import asyncio
adminperms = [712639419785412668, 268103439614083074, 867751309923188737, 369197839680536576]
TOKEN = open("../TOKEN", "r")

async def devcommands(x, message):
    if not message.author.id in adminperms:
        print("nu")
        return
    command = x[0]
    match command:
        case "echo":
            await message.channel.send(" ".join(x[1:]))

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self, message):
        content = message.content
        print(content)
        if content.startswith("!dev "):
            content = content.split(" ")
            await devcommands(content[1:], message)
        elif content.startswith("!"):
            await commandprovider(content[1:], message)




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(
    TOKEN.read())
