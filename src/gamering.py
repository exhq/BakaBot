import random


def winner(player_choice, computer_choice):
    if player_choice == 'rock' and computer_choice == 'scissors':
        return True
    elif player_choice == 'scissors' and computer_choice == 'paper':
        return True
    elif player_choice == 'paper' and computer_choice == 'rock':
        return True
    else:
        return False


async def rps(x, message):
    item = ["rock", "paper", "scissors"]
    bruh = random.randint(0, 2)
    no = item[bruh]
    if x == no:
        await message.channel.send(f"""
            you chose {x}, i chose {item[bruh]}. its a tie lmao.
            """)
        return
    if x not in item:
        if bool(bruh):
            await message.channel.send(f"""
 you chose {x}, i chose {item[bruh]}. i win.
 """)
        else:
            await message.channel.send(f"""
 you chose {x}, i chose {item[bruh]}. you win.
 """)
    else:
        if winner(x, random.choice(item)):
            await message.channel.send(f"""
            you chose {x}, i chose {item[bruh]}. you win.
            """)
        else:
            await message.channel.send(f"""
            you chose {x}, i chose {item[bruh]}. i win.
            """)
