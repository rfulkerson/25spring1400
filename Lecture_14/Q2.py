my_list = [1, 909, 3, 6]
x = int(input('Enter a number: '))

# print(id(x))
# print(id(my_list[1]))

if x in my_list:
    print('In', end=' ')
if x is my_list[1]:
    print('Is')

