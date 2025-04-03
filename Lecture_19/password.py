import random

source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-={}[]|\':;<,>.?/"
password = ""
howmany = 30
x = 0

while x < howmany:
    #pick position
    which = random.randint(0,len(source)-1)
    #pick a letter out of source
    #print(source[which])
    password += source[which]
    x += 1

print(password)