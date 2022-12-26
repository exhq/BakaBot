import pathlib
from discord.ext.commands import Bot, check, Context
blacklist = pathlib.Path('block')
async def qblock(context: Context):
    blacklist.write_text("".join(context.message.content.split(" ")[2]))
    await context.reply("link has been blacklisted")
