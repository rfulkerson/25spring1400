import random

source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# source = "abcdefghijklmnopqrstuvwxyz"

password = ""
howlong = 5

for x in range(howlong):
    which = random.randint(0,len(source)-1)
    password += source[which]

print(password)

# crack the password

for a in source:
    for b in source:
        for c in source:
            for d in source:
                for e in source:
                    guess = f'{a}{b}{c}{d}{e}'
                    if guess == password:
                        print(f'Your password is {guess}')
    

    
# which = random.randint(0,len(source)-1)
# password += source[which]
# which = random.randint(0,len(source)-1)
# password += source[which]
# which = random.randint(0,len(source)-1)
# password += source[which]

# print(password)