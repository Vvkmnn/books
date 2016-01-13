#!/usr/bin/env python3
# Lecture 8: Python's Built-In Functions
"""Lecture 8 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

import random
import pyperclip
import sys

random.randint(10, 20)

pyperclip.copy('Hello world!')
pyperclip.paste()
sys.exit()

# Recap:
# - You can import modules and get access to new functions.
# - The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool.
# - The sys.exit() function will immediately quit your program.
# - The pyperclip third-party module has copy() and paste() functions for reading and writing text to the clipboard.
