import random
from discord.ext import commands
from discord.ext.commands import Context, command
from random import randint

coin = 1



@command()
@commands.cooldown(1.0, 300.0, commands.BucketType.user)
async def mine(context: Context,):
    global coin
    coin +=1
    coint =str(coin)
    text ="You bakas have "
    text +=coint
    text +="bakacoin."
    await context.send(text) 

@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
async def balance(context: Context,):
    global coin
    if coin == 1000:
        text ="everythingonarm they did it !!!!!! look!!!!"
    elif coin <= 1000:
        coint =str(coin)
        text = coint
        text +="bakacoin"
    else:
        text ="everythingonarm they did it !!!!!! look!!!!"
    await context.send(text) 
    
@command()
@commands.cooldown(1.0, 150.0, commands.BucketType.guild)
async def invest(context: Context,):
    global coin
    winchance = randint(1, 5)
    win = 2
    if winchance >= win:
        coin = coin * 2
    else:
        coin = coin / 2
    coint =str(coin)
    text ="You bakas have "
    text +=coint
    text +="bakacoin."
    await context.send(text) 
    
@command()
@commands.cooldown(1.0, 30.0, commands.BucketType.guild)
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
