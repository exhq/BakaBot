import random

from discord.ext.commands import Context, command


@command()
async def rps(context: Context, *, player_choice: str):
    player_choice = player_choice.replace("https://", "").replace("http://", "").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    text = f"you chose {player_choice}, i chose {computer_choice}. "

    if player_choice == computer_choice:
        text += "its a tie lmao"
    elif player_choice == "rock" and computer_choice == "scissors":
        text += "you win"
    elif player_choice == "paper" and computer_choice == "rock":
        text += "you win"
    elif player_choice == "scissors" and computer_choice == "paper":
        text += "you win"
    elif player_choice in options:
        text += "i win"
    else:
        text += random.choice(["i win", "you win"])

    await context.send(text)
