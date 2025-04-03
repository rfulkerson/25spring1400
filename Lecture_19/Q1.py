import random

def generate():
    values = []
    for a in range(5):
        v = random.randint(1,3)
        values.append(v)
    # no return statement here ... function returns nothing
    # when a function doesn't have a return statement, it's
    # known as a void function. void functions have None as
    # a return value.

print(generate())

# generate()
# x = generate()
# print(x)
# 