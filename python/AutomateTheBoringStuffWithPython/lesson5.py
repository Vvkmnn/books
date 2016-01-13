#!/usr/bin/env python3
# Lecture 5: If, Else, and Elif Statements
"""Lecture 5 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

name = 'Bob'
if name == 'Alice':
    print('Hi Alice')
print('Done')

password = 'swordfish'
if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password.')

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

print('Enter a name.')
name = input()
if name != '':
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')

# Recap:
# - An if statement can be used to conditionally execute code, depending on whether or not the if statement's condition is True or False.
# - An elif ("elise if") statement can follow an if statement. Its block executes if its condition is True and all the previous conditions have been False.
# - An else statement comes at the end. It's block is executed if all the previous conditions have been False.
# - The values 0, 0.0, and the empty string are considered Falsey values. When used in conditions they are considered False. You can always see for yourself which values are Truthy or Falsey by passing them to the bool() function.
