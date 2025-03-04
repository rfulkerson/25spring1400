# Generate a randomized password consisting of 8 random lowercase letters.
# Modify the code to also incorporate uppercase letters.
# Modify the code to also incorporate punctuation marks.

# We'll need tools from the random library and the material from lecture 6 (strings).

import random

#source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_=+:?"
source = ["green","cat","potato","yellow"]
howmany = int(input("How long would you like your password? "))
x = 0

while x < howmany:
    source_length = len(source)
    which = random.randint(0,source_length-1)
    print(source[which], end="")
    x = x + 1
    