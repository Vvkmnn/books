#!/usr/bin/env python3
# Lecture 10: Global and Local Scopes
"""Lecture 10 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'


def spam():
    global eggs
    eggs = 'Eggs'
    print(eggs)


def bacon():
    eggs = 10
    print(eggs)

eggs = 42

print(eggs)  # global print
bacon()  # local print
spam()  # local print with global assignment
print(eggs) # global print after global assignement


# Recap:
# - A scope can be thought of as an area of the source code, and as a container of variables.
# - The global scope is code outside of all functions. Variables assigned here are global variables.
# - Each function's code is in its own local scope. Variables assigned here are local variables.
# - Code in the global scope cannot use any local variables.
# - Code in a function's local scope cannot use variables in any other function's local scope.
# - If there's an assignment statement for a variable ina  function, that is a local variable.
