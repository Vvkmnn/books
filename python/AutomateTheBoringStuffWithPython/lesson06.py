#!/usr/bin/env python3
# Lecture 6: While Loops
"""Lecture 6 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

# spam = 0
# while spam < 5:
#    print('Hello world!')
#    spam = spam + 1

#name = ''
#while name != 'your name':
#    print('Please type your name.')
#    name = input()
#print('Thank you!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

# Recap:
# - When the execution reaches the end of a while statement's block, it jumps back to the start to re-check the condition.
# - Press Ctrl-C to interrupt an infinite loop.
# - A break statement causes the execution to immediately leave the loop without re-checking the condition.
# A continue statement causes the exeuction to immediately jump back to the start of the loop and re-check the condition.
