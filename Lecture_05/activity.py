# today's activity

# Input the temperature in degrees Celsius and
# convert to Fahrenheit:
# ℉=(9/5)℃+32

deg_cel = float(input("Enter Celsius temp: "))
deg_fah = (9 / 5) * deg_cel + 32
print(f"{deg_cel:.2f} Celsius is {deg_fah:.2f} Fahrenheit")


# Input the temperature in degrees Fahrenheit and
# convert to Celsius:
# ℃=(5/9)(℉ −32)

deg_fah = float(input("Enter Fahrenheit temp: "))
deg_cel = (5 / 9) * (deg_fah - 32)
print(f"{deg_fah:.2f} Fahrenheit is {deg_cel:.2f} Celsius")

