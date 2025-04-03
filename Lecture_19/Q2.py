def determine(inc):
    if 9876 <= inc <= 40125:
        taxRate = 0.12
    elif  40126 <= inc <= 85525:
        taxRate = 0.22
    elif 0 < inc <= 9875:
        taxRate = 0.10
    else:
        taxRate = 0.24
    return taxRate

# 0, 1, 9874, 9875, 9876, 40124, 40125, 40126, 85524, 85525, 85526, -1234, 12312341234

print(determine(9874))
print(determine(9876))
print(determine(40125))
print(determine(85525))
print(determine(100000))


# value = int(input())
# if value > 0:
#     x = determine(value)
#     print("Tax rate is", x)
# else:
#     print("Can't determine tax rate")
