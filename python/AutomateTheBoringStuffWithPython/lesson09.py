#!/usr/bin/env python3
# Lecture 9: Writing Your Own Functions
"""Lecture 9 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

# Built in Python Functions
# print()
# len()
# input(prompt=None)

# import sys


def Hello(name):
    print('Hello ' + name)


def plusOne(number):
    return number + 1


Hello('Alice')
Hello('Bob')

print('Hello has ' + str(len('hello')) + ' letters in it.')

newNumber = plusOne(5)
print(newNumber)

# Recap:
# - Functions are like mini-pgroams inside your program.
# - TThe main point of functions is to get rid of duplicate code.
# - The def statement defines a function.
# - The input to functions are arguments. The output is the return value.
# - The parameters are the variables in between the function's parentheses in the def statement.
# - The return value is specified using the return statement.
# - Every function has a return value. If your function doesn't have a return statement, the default return value is None.
# - Keyword arguments to functions are usually for optional arguments. The print() function has keyword arguments end and sep.
