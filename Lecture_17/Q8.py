def other(num):
    return num + 25

def thing(a, b):
    return other(a) + other(b)

print(thing(10,20))
