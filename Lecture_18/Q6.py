def multiply_and_add(a, b):
    return (a * 2) + (b * 3)

def evaluate(a, b):
    result = ""
    if multiply_and_add(a, b) > a + b:
        result = "larger"
    else:
        result = "smaller"
    return result

print(evaluate(2, 3))