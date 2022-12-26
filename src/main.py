import discord
from discord import Message
from discord.ext.commands import Bot, check, Context

from src import alias as aliases
from src import gamering

adminperms = [712639419785412668, 268103439614083074,
              867751309923188737, 369197839680536576,
              310702108997320705]
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


@client.group(pass_context=True, invoke_without_command=True)
@dev_only
async def dev(context: Context):
    await context.send("Unknown dev command")


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
