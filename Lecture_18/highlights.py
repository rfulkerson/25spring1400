# highlights from lecture 18

# for x in range(5):
#     print("Hello")
# 
# def greeting():
#     print("Hello there")
# 
# for x in range(5):
#     greeting()

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

def isOdd(z):
    return z % 2 != 0
    
if __name__ == '__main__':
    y = int(input("Enter a number: "))
    if isEven(y):
        print(f"{y} is an even number.")

    if isOdd(y):
        print(f"{y} is an odd number.")
    
    