def determine(inc):

    taxRate = 0.24
    
    if inc <= 0:
        taxRate = 0.00
    elif inc <= 9875:
        taxRate = 0.10
    elif inc <= 40125:
        taxRate = 0.12
    elif inc <= 85525:
        taxRate = 0.22


    return taxRate

print(determine(125000))

# -1, -1234, 0, 9874, 9875, 9876,
# 40124, 40125, 40126, 85524, 85525, 85526,
# 125000, 1234123412341234,

# 40125.01
# 40125.0000000000001

#print(determine(12500))
