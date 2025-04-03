# highlights from lecture #16

from random import randint

target = randint(1,100)

#print(target)

guess = int(input("Enter your guess 1-100: "))
count = 1

while guess != target:
    count += 1
    if guess < target:
        print("Your guess is too small! Try again!")
    elif guess > target:
        print("Your guess is too large! Try again!")
    guess = int(input("Enter your guess 1-100: "))
    
print(f"You guessed {guess} in {count} attempts! Way to go! You're awesome!")
    

