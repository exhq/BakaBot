import datetime
import pathlib

from discord import Message

timer_file = pathlib.Path('timer')


async def checkformessages(message: Message):
    if timer_file.exists():
        last_timestamp = float(timer_file.read_text().strip())
        last_timestamp = datetime.datetime.fromtimestamp(last_timestamp)
        time_passed = datetime.datetime.now() - last_timestamp
        if time_passed < datetime.timedelta(seconds=300):
            return

    if " touhou " in message.content:
        await message.reply("https://cdn.discordapp.com/attachments/918571405212270652/1056934396852191343/to_ho.mp4")
        return

    if " rent " in message.content:
        await message.reply("https://media.discordapp.net/stickers/1009434642123870298.png")
        return

    timer_file.write_text(str(datetime.datetime.now().timestamp()))
