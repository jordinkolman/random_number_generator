'''
Guess The Number Game

Created on Jul 22 10:00 2022

@author: Jordin Kolman

'''

import random


def random_game():
    user_guess = 0
    random_number = random.randint(1, 20)
    play_again = 'y'
    user_tries = 0

    user_name = input("Welcome to the Random Number Guessing Game! Please enter your name: ")
    print("Hello", user_name)
    while play_again == 'y':
        user_guess = int(input("Please guess a number between 1 and 20: "))
        if user_guess >= 21 or user_guess <= 0:
            print("ERROR: Guess must be between 1 and 20. Try again. ")
            play_again = 'y'
        else:
            if user_guess == random_number:
                user_tries = user_tries + 1
                print("Congratulations! You have guessed correctly. It took you", user_tries, "tries.")
                play_again = input("Would you like to play again? (y/n): ").lower()
                random_number = random.randint(1,20)
            elif user_guess < random_number:
                print("Your guess was too low. Try again!")
                user_tries = user_tries + 1
            elif user_guess > random_number:
                print ("Your guess was too high. Try again!")
                user_tries = user_tries + 1
    print("Thank you for playing", user_name + ". Have a good day!")

random_game()
