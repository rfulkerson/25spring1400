
# this was similar to code from some MSPs; very long print() statements
print(f'{(x/7+1.24)/100:.2f}', f'{(x/7+3.24)/100:.2f}', f'{(x/7+6.24)/100:.2f}')

# here's a slightly shorter/easier way
print(f'{(x/7+1.24)/100:.2f}', end=" ")
print(f'{(x/7+3.24)/100:.2f}', end=" ")
print(f'{(x/7+6.24)/100:.2f}')

# or approach it like this by separating arithmetic from presentation
first = (x/7+1.24)/100
second = (x/7+3.24)/100
third = (x/7+6.24)/100

print(f'{first:.2f}', end=" ")
print(f'{second:.2f}', end=" ")
print(f'{third:.2f}')

# a slightly shorter way to do the above three print() statements
print(f'{first:.2f} {second:.2f} {third:.2f}')
