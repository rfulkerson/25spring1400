# def print_price(item, cost):
#     print(f'{item} cost ${cost:.2f}')

def print_price(item, cost):
    print(f'{item:>15}  ${cost:.2f}')

print_price("Beans", 1.23)
print_price("Corn", 0.59)
# print_price("Detergent", 8.92)
# print_price("baby spinach", 1.29)