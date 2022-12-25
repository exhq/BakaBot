import random


async def rps(x, message):
    x = x.replace("https://", "").replace("http://", "")
    options = ["rock", "paper", "scissors"]
    computer_choice = options[random.randint(0, len(options)-1)]
    computer_choice_index = options.index(computer_choice)
    lmao = random.choice(["i win", "you win"])

    if x == options[computer_choice_index]:
        await message.channel.send(f"you chose {x}, i chose {options[computer_choice_index]}. its a tie lmao")
    elif x == "rock" and options[computer_choice_index] == "scissors":
        await message.channel.send(f"you chose {x}, i chose {options[computer_choice_index]}. you win")
    elif x == "paper" and options[computer_choice_index] == "rock":
        await message.channel.send(f"you chose {x}, i chose {options[computer_choice_index]}. you win")
    elif x == "scissors" and options[computer_choice_index] == "paper":
        await message.channel.send(f"you chose {x}, i chose {options[computer_choice_index]}. you win")
    elif x in options:
        await message.channel.send(f"you chose {x}, i chose {options[computer_choice_index]}. i win")
    else:
        await message.channel.send(f"you chose {x}, i chose {options[computer_choice_index]}. " + lmao)
