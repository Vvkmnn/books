#!/usr/bin/env python3
# Lecture 15: List Methods
"""Lecture 15 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

spam = ['hello', 'hi', 'howdy', 'heya']

#  Methods are inherited functions.

spam.index('hello')

# .index does not work

spam.index('heya')

cats = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']

# only first instance in the list is returned

cats.index('Pooka')

animals = ['cat', 'dog', 'bat']

# append values to the end
print(animals)

animals.append('moose')

print(animals)

# insert value at index value
print(animals)

animals.insert(1, 'chicken')

print(animals)

# spam = spam.append(value) rewrites the list, do not use this, just the method

eggs = 'hello'
# eggs.append('world') this raises error, because strings dont have append

animals2 = ['cat', 'bat', 'rat', 'elephant']

print(animals2)
animals2.remove('bat')
print(animals2)
# animals2.remove('bat') throws error, already removed.


animals3 = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
animals3.remove('cat')
print(animals3)
# only removes the first instance of 'cat'

numbers = [-7, 1, 2, 3.14, 1, -7]

print(numbers)

numbers.sort()

print(numbers)

numbers.sort(reverse=False)

print(number)
# sort works on numbers and strings, but not when they are in the same list.

animalsandnumbers = animals + numbers
# animalsandnumbers.sort() is an error.

nouns = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
print(nouns)
nouns.sort()
print(nouns)

# Python uses ASCII sorting, which puts lowercase letters in front always

nouns.sort(key=str.lower)
print(nouns)
# Recap:
# - Methods are functions that are "called on"  values.
# - The index() list method returns the index of an item in the List.
# - The append() list method adds a value anywhere inside a list.
# - The insert() list method removes an item, specified by the value, from a list.
# - The sort() method reverse=True keyword argument can sort in reverse order.
# - Sorting happens in "ASCII-betical" order. To sort normally, pass key=str.lower.
# - These list methods operate on the list "in place", rather than returning a new list value.
