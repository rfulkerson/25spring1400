# One way to write an isEven() function
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

# refactoring to have a single return
def isEvenTwo(x):
    result = False
    if x % 2 == 0:
        result = True
    return result

# doing it in one step
def isEvenThree(x):
    return x % 2 == 0

# using the last isEvenThree() as a model for factors
def isFactor(x, y):
    return x % y == 0

# handle any collection or string to see if it's empty
def isEmpty(m):
    return len(m) == 0

# a little it of example code
value = int(input())
if value % 2 == 0:
    print("That's even!")
    
if isEven(value):
    print("That's even!")