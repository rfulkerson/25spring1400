def function_a():  # global function
    x = 12    # local variable
    print(x)
    function(b)

def function_b():  # global function
    y = 42.123  # local variable
    print(y)
    for z in range(6):    # z is local variable, range is a built-in function
        print(z)
    function_a()

if __name__ == '__main__':
    z = int(input())  # local variable
    print(z)  # print is a built-in scope function
    function_a()
    function_b()
