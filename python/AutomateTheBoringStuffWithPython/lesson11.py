#!/usr/bin/env python3
# Lecture 11: Handlng Errors with try/except
"""Lecture 11 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'


def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')


print(div42by(2))
print(div42by(12))
print(div42by(0))  # error from divide by 0; stops entire program. So add a try/except statement to divideBy.
print(div42by(1))

print('How many cats do you have?')

numCats = input('>')

try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')


# Recap:
# - A divid-by-zero happens when Python divides a number by 0.
# - Errors cause the program to crash.
# - An error that happens inside a try block will cause code in the except block to execute. That code can handle the error or display a message to the user so that the program can keep going.
