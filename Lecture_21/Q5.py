gas = {"Casey's" : 2.99,
       "Costco" : 2.84 }
print("12345678901234567890")
for loc in gas:
    print(f"{loc:12}{gas[loc]:6.2f}")
    #print(f"{loc:12}{gas[loc]:2.6f}")
    #print(f"{loc:>12}{gas[loc]:^6.2f}")
    #print(f"{loc:^12}{gas[loc]:6.2f}")
