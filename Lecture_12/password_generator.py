import random

x = 0

source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@##$%^&*()_+-=}{"

while x < 20:
    #print("Hi")
    #print(random.randint(0,25))
    pos = random.randint(0,len(source)-1)    # generate 0 to 25
    #print(pos, source[pos])
    print(source[pos], end="")
    x += 1