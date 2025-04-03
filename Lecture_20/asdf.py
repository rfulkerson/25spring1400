def function_1(x):
    print(x)
    x = 7
    

z = 5
function_1(z)   # immutable argument
print(z)

y = [6,1,7]
function_1(y)   # mutable argument
print(y)