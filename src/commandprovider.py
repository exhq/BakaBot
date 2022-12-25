import gamering


async def commandprovider(x: str, message):
    x = x.split(" ")
    if x[0] == "rps":
        await gamering.rps(" ".join(x[1:]), message)
