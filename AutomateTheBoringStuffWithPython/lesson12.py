#!/usr/bin/env python3
# Lecture 12: Writing a "Guess the Number Program"
"""Lecture 12 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

# This is a guess the number game.

import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
SecretNumber = random.randint(1, 20)

# print('Debug: The Secret Number is ' + str(SecretNumber))

for guessesTaken in range(1, 7):
    try:
        print('Take a guess.')
        guess = int(input())

        if guess < SecretNumber:
            print('Your guess is too low.')
        elif guess > SecretNumber:
            print('Your guess is too high.')
        else:
            break  # This condition is for the correct guess.
    except ValueError:
        print('Please enter a number.')

if guess == SecretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(SecretNumber) + '.')
print('You took ' + str(guessesTaken) + ' guesses.')

# Recap:
# - Cover all concepts from previous lessons for Python Recipe.
