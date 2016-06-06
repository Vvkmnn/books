#!/usr/bin/env python3
# Lecture 3: Writing Our First Program
"""Lecture 3 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

# This program says Hello and asks for my name

print('Hello World')
print('Whats is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('Whats is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')

# Recap:
# - Type programs into the file editor
# - The execution starts the top and moves down
# - # Comments are ignored by Python
# -  Functions are mini-programs iny our program
# - print() displays the value passed into it
# - intput() lets user type in a value
# - len() takes a string value and returns an integer value of the string's length
# - int(), str(), and float() convert value's data type
