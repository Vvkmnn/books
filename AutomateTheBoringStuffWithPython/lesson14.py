#!/usr/bin/env python3
# Lecture 14: For Loops with Lists, Multiple ASsignment, and Augmented Operators
"""Lecture 14 of "Automate the Boring Stuff with Python."""
__author__ = 'Vivek Menon'

for i in range(4):
    print(i)

range(0, 4) == [0, 1, 2, 3]

spam = list(range(0, 100, 2))

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']


def supplyList(supplies):
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

supplies2 = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']

supplyList(supplies)
supplyList(supplies2)

cat = ['fat', 'orange', 'loud']

size, color, disposation = cat  # assign variables to values in a list

print(color)   # evaluates to orange
print(size)  # evaluates to fat
print(disposation)  # evaluates to loud

size, color, disposation = 'skinny', 'black', 'quiet'

print(color)   # evaluates to skinny
print(size)  # evaluates to black
print(disposation)  # evaluates to quiet

a = 'AAA'
b = 'BBB'

print(a)
print(b)
a, b = b, a  # swap strings and variables with mutliple assignment
print(a)
print(b)

spam2 = 42
spam = spam + 1

spam += 1  # increment itself by 1!
spam -= 1  # subtract itself by 1!
spam *= 1  # multiply itself by 1!
spam /= 1  # divide itself by 1!
spam %= 1  # modulo itself by 1!


# Recap:
# - For loops technically iterate over the values in a list.
# - The range() function returns a list-like value, which can be passed to the list() function if you neeed an actual list value.
# - Variables can swap their values using multiple assignment.
# - Augmented assignment operaters like += are used as shortcuts.
