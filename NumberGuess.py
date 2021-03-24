# Created by Jacob Huffman

import random

randNum = random.randint(1, 100)
guesses = 0
name = raw_input("What is your name? ")

for i in range(1, 9):
    guesses = guesses + 1
    print("Howdy " + name + " " + "guess a number 1-100! \n")
    guess = str(input())

    if guess.isdigit():
        if int(guess) > randNum:
            print("your guess is too high \n")

        elif int(guess) < randNum:
            print("your guess is too low \n")

        elif int(guess) == randNum:
            print("dude you're a genius \n")
            print("you needed " + str(guesses) + " guesses")
            break

        if guesses == 8:
            print("You ran out of guesses!")
            print("THE RANDOM NUMBER WAS......")
            print
            print("|")
            print("V")
            print
            print(randNum)

    else:
        print("Invalid Input! Try a number. \n")
