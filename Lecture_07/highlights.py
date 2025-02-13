# highlights from lecture 7

expression = input("Enter expr: ")
print(expression)

# string: 6 + 7
#         01234

left = float(expression[0])
right = float(expression[4])
operator = expression[2]

print(left,operator,right)

result = 0.0

if operator == "+":
    result = left + right
elif operator == "-":
    result = left - right
elif operator == "*":
    result = left * right
elif operator == "/":
    result = left / right
elif operator == "%":
    result = left % right
elif operator == "^":
    result = left ** right

print(left,operator,right,"=",f"{result:.2f}")


