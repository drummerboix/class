'''
ROCK PAPER SCISSORS Project by ADEDAMOLA OGUNBONA
version 2.0
'''

# random stuff
from random import *

# Enter player name
player_name = input("Hi human! What is your name? ")
# List of options
stuff = [('Rock' or 'rock'), ('Paper'or 'paper'), ('Scissors' or 'scissors')]

# Boolean for player
player = False

while player == False:
    player = input("Alright %s! Rock, Paper, Scissors? " %player_name)
    pc = stuff[randint(0,2)]
    # check random value
    #print(pc) 
    if player == pc:
        print("It's a tie mate")
    elif player == "quit":
        break
    # Conditions for paper
    elif (player == "Paper") or (player == "paper"):
        if (pc == "Scissors") or (pc == "scissors"):
            print("You lose, %s cuts %s" %(pc, player))
        elif (pc == "Rock") or (pc == "rock"):
            print("You win, %s covers %s" %(player, pc))
    # Conditions for Scissors
    elif (player == "Scissors") or (player == "scissors"):
        if (pc == "Rock") or (pc == "rock"):
            print("You lose, %s smashes %s" %(pc, player))
        elif (pc == "Paper") or (pc == "paper"):
            print("You win, %s cuts %s" %(player, pc))
    # Conditions for Rock
    elif (player == "Rock") or (player == "rock"):
        if (pc == "Paper") or (pc == "paper"):
            print("You lose, %s covers %s" %(pc, player))
        elif (pc == "Scissors") or (pc == "scissors"):
            print("You win, %s smashes %s" %(player, pc))
    else:
        print("Not a valid option mate!, try again!")
        #continue
    # Start over
    player = False
    #pc = stuff[randint(0,2)]

    