#!/usr/bin/env python3
# Lecture 13: The List Data Type
"""Lecture 13 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

spam = ['cat', 'bat', 'rat', 'elephant']

spam
spam[0]
spam[1]
spam[2]
spam[3]

spam2 = [['cat', 'bat'], [10, 20, 30, 40, 50]]

spam2[0][1]  # evaluates to cat
spam2[1][4]  # evaluates to 50

spam[-1]  # evaluates to elephant
spam[-2]  # evaluates to rat

spam[1:3]  # slice of List

spam3 = [10, 30, 30]

spam3[1] = 'Hello'

print(spam3)

spam3[1:3] = ['CAT', 'DOG', 'MOUSE']

print(spam3)

print(spam[:2])  # skip notation for first value, go to second value

print(spam[1:])  # skip notation for the end value, go from start to end

del(spam[2])

print(spam)

len([1, 2, 3])


print('Hello' * 3)

print([1, 2, 3] * 3)

print(list('Hello'))

'howdy' in ['hello', 'hi', 'howdy', 'heyas']

'howdy' not in ['hello', 'hi', 'howdy', 'heyas']

# Recap:
# - A list is a value that contains multiple values.
# - The values in a list are also called items.
# - You can access items in a list with it's integer index.
# - The indexes start at 0, not 1.
# - You can also use negative indexes. -1 refers to the last item, -2 refers to the second to last item, and so on.
# - You can multiple items from the list using a slice.
# - The slice has two indexes. The new list's items start at the first index and go up to, but doesn't include, the second index.
# - The len() function, concatenation, and replication work the same way with lists as they do with strings.
# - You can convert a value into a list by passing it to the list() function.
