

import discord
from discord.ext.commands import Bot, check, Context

TOKEN = open("../TOKEN", "r")


intents = discord.Intents.default()
intents.message_content = True

client = Bot(intents=intents, command_prefix="!")


@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')

@client.command(pass_context=True, invoke_without_command=True)
async def ping(context: Context):
    await context.reply("hello im not a bad person and i dont swear")



client.run(TOKEN.read())
