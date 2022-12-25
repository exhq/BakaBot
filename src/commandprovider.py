import gamering
async def commandprovider(x: str, message):
    x = x.split(" ")
    match x[0]:
        case "rps":
            await gamering.rps(x[1], message)
