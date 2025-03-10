my_list = ["Jeff", "Emi", "Mohammed", "Ella"]

x = input('Enter a name: ')

# print(id(x))
# print(id(my_list[0]))

if x in my_list:
    print('In', end=' ')
if x is my_list[1]:
    print('Is')
