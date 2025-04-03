def get_values():
    print("Enter 10 values:")
    
    values = []

    for counter in range(10):
        v = int(input())
        values.append(v)
    
    return values
    
my_list = get_values()
print(max(my_list))