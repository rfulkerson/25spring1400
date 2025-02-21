one = -1
two = 2
three = 3
four = 4

result = four > 10 or (two < 0 and three > 10) or one < 0


if one < 0 or two < 0 and three > 10 or four > 10:
    pass

# a = (one < 0 or two < 0) and (three > 10 or four > 10)
# b = (one < 0 or ((two < 0 and (three > 10 or four > 10))
))
# c = (one < 0 or (two < 0 and three > 10) or four > 10
)
# d = (((one < 0 or two < 0) and three > 10) or four > 10)
