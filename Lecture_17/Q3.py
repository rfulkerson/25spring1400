def a_function():
    return "foo"

for a in range(4):
    # print(a_function())
    # result = a_function()
    # print(f'{a}{result}', end=" ")
    if a_function() == "foo":
        print("Hi!")