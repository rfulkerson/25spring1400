x = float(input("enter a number: "))

if 0 <= x <= 10:
    print(f"{x} appears to be between 0 and 10.")
else:
    print(f"{x} does not fit the criteria.")

if x >= 0 and x <= 10:
    print(f"{x} appears to be between 0 and 10.")
else:
    print(f"{x} does not fit the criteria.")
    
if 0 <= x and x <= 10:
    print(f"{x} appears to be between 0 and 10.")
else:
    print(f"{x} does not fit the criteria.")
