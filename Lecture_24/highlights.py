# highlights from lecture 24

a = [7, 1234, 1234,651345, 10]

# for x in a:
#     print(x)
#     
# print()

# for x in a:
#     x *= 2
#     print(x)
# 
# print(a)

# 
# 
# for pos in range(0,len(a)):
#     a[pos] *= 2
#     
# print(a)
#

a = [7, 1234, 1234,651345, 10]

b = [ x % 2 == 0 for x in a ]

print(b)
print(a)

b = []
for x in a:
    if x % 2 == 0:
        b.append(True)
    else:
        b.append(False)
print(b)
print(a)
# 
# 
# a = [ x * 2 for x in a ]
# 
# print(a)
# 
# names = ["Maverick", "Husker", "Hawkeye"]
# 
# print(names)
# names = [ u + "s" for u in names ]
# print(names)
# 
# print(a)
# 
# less_than = [ y for y in a if y < 100 ]
# 
# print(less_than)
# 
# lt = []
# for y in a:
#     if y < 100:
#         lt.append(y)
#         
# print(lt)
