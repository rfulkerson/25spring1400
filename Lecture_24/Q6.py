sentence = input()
words = sentence.split()
stuff = [x.isdecimal() for x in words]
print(stuff)

# stuff = [x.isdecimal() for x in input().split()]
# print(stuff)

