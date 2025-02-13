x = int(input())

if x >= 0:
    print("Hello")
elif x < 20:
    print("Goodbye")
else:
    print("What's up?")

# should test:
# negative values
# 0
# -1
# 1
# something between 0 and 20
# 19
# 20
# 21
# something really big