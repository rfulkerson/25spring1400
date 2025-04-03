def send_an_int(x):
    print('in before',x)
    x = x + 10
    print('in after',x)
    
def send_a_list(a):
    print('in before',a)
    # creates a brand new list ...
    #y = ["Hello","world",2112]
    # accesses the old list by reference
    a[0] = 500 
    print('in after',a)
    
if __name__ == '__main__':

    y = [10, 20, 30]
    print('out before', y)
    send_a_list(y)
    print('out after', y)

#     x = 17
#     print('out before',x)
#     send_an_int(x)
#     print('out after',x)