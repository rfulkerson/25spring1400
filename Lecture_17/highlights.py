# highlights from lecture 17



















exit()
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even!")

num2 = int(input("Enter a number: "))
if num2 % 23 == 0:
    print(f"{num2} is even!")

num3 = int(input("Enter a number: "))
if num3 % 2 == 0:
    print(f"{num3} is even!")

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
 
number = int(input("Enter a number: "))
if isEven(number):
    print(f"{number} is even!")

num2 = int(input("Enter a number: "))
if isEven(num2):
    print(f"{num2} is even!")

num3 = int(input("Enter a number: "))
if isEven(num3):
    print(f"{num3} is even!")
    
def isEvenAlternate(x):
    result = False
    if x % 2 == 0:
        result = True
    return result

def isEvenAnother(x):
    return x % 2 == 0
