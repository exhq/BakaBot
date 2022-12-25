import random


def winner(player_choice, computer_choice):
    if player_choice == 'rock' and computer_choice == 'scissors':
        return 1
    elif player_choice == 'scissors' and computer_choice == 'paper':
        return 1
    elif player_choice == 'paper' and computer_choice == 'rock':
        return 1
    elif player_choice == computer_choice:
        return 2
    else:
        return 3


async def rps(x, message):
    bruh = random.randint(0, 2)
    print(x)
    item = ["rock", "paper", "scissors"]
    if message == random.choices(item):
        await message.channel.send(f"""
            you chose {x}, i chose {item[bruh]}. lmao its a tie
            """)
        return
    if x not in item:
        if bruh == 1:
            await message.channel.send(f"""
you chose {x}, i chose {item[bruh]}. i win.
""")
        else:
            await message.channel.send(f"""
you chose {x}, i chose {item[bruh]}. you win.
""")
    else:
        if winner(x, random.choice(item) == 1):
            await message.channel.send(f"""
            you chose {x}, i chose {item[bruh]}. you win.
            """)
        elif winner(x, random.choice(item) == 3):
            await message.channel.send(f"""
            you chose {x}, i chose {item[bruh]}. i win.
            """)
        else:
            await message.channel.send(f"""
            you chose {x}, i chose {item[bruh]}. lmao its a tie
            """)
