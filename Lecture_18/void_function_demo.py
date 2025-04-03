# a function that returns a value of 7
def one_function():
    return 7

# a void function that does something but doesn't return anything
def two_function():
    print("Hello")
    
# example function calls
x = one_function()
print(x) # should print 7
y = two_function()
print(y) # should print None (indicating that nothing was returned)