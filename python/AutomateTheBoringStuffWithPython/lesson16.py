#!/usr/bin/env python3
# Lecture 16: Similarities Between Lists and Strings
"""Lecture 16 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

list('Hello')

name = 'Zophie'

name[0]

name[1:3]

name[-2]

'Zo' in name

'XXX' in name

for letter in name:
    print(letter)

# Lists are mutable; they can be changed.
# Strings are immutable; they cannot be changed.

name[7]

# name[7] = 'x' throws error, cant change letter in a string.

name = 'Zophie a cat.'
newName = name[0:7] + 'the' + name[8:]

spam = [0, 1, 2, 3, 4, 5]
cheese = spam

cheese[1] = 'Hello!'
print(cheese)  # First variable is change to hello
print(spam)  # spam changed too, because spam is pointed to cheese; changes every reference to the list.

# Immutable items are not references, so they have to be changed absolutely.

def eggs(someParameter):
    someParameter.append('Hello!')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# changes to global variable from a local scope change. Because it's a list reference, it works. Mutable data types are references, and can be changed by any method calls, etc.

# for a completely seperate list, we can use copy.deepcopy()

import copy

letters = ['A', 'B', 'C', 'D']

letters2 = copy.deepcopy(letters)

letters2[1] = 42

print(letters2)
print(letters)

# These are now seperate lists, and can be modified seperately because they are stored in different places. References are used a short version to point to different file.

fruits = [
    'apples',
    'oranges',
    'bananas',
    'coconuts']

# Lists can be continued across multiple lines.

# Recap:
# - Strings can do a lot of the same things lists can do, but strings are immutable.
# - Immutable values like strings and tuples cannot be modified "in place".
# - Mutable values list lists can be modified in place.
# - Variables don't contain lists, they contain references to lists.
# - When passing a list argument to a function, you are actually passing a list reference.
# - Changes made to a list in a function will affect the list outside the function.
# - The \ line continuation character can be used to stretch Python instructions across multiple lines.
