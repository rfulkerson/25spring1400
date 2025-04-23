names = []
n = input("Enter name: ")
while n != "done":
    names.append(n)
    n = input("Enter name: ")
names.sort(reverse=False, key=str.lower)
print(names)




#names.sort(reverse=False, key=str.upper)

# monica
# Chandler
# ross
# Phoebe
# done