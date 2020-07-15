# Guess the number game by ADEDAMOLA OGUNBONA

# for random generation
from random import *

# # your guess
# user = int(input("Enter your guess: "))
# # random number
# prog_guess = randint(0,10)
# run = True

# def Guess_stuff():
#     if prog_guess == user:
#         print("Good job mate")
#     elif prog_guess < user:
#         print("Guess again mate, too high")
#     else:
#         print("Guess again mate, too low")

#     print("The correct answer is %i" %prog_guess)

# while run:
#     Guess_stuff()

# starters for the while loop
original = 0
# variable for while loop, accepts true or false
run = True

player_name = input("Hi human! What is your name? ")
count = 0

def Guess_stuff():
    # pull original and run into the function
    global original
    global run
    global count
    # generate random number for the program
    prog_guess = randint(0,20)
    # empty user input
    user = []
    if original == 0:
        if count == 0:
            user = input("Ok %s, guess a number between 0 and 20: " %player_name)
        else:
            user = input("Try again: ")
    else:
        user = input(str(original))

    # break the program if user enters quit
    if user == "quit":
        print("Goodbye human!")
        run = False
    else:
        # if guess is correct
        if prog_guess == int(user):
            print("Good job mate!")
        elif prog_guess < int(user):
            print("Guess again mate, too high")
        elif prog_guess > int(user):
            print("Guess again mate, too low")
        print("Correct answer is %i" %prog_guess)
        count += 1

    if count > 5:
        print("Damn %s, you've done this %i times" %(player_name, count))

while run:
    Guess_stuff()

