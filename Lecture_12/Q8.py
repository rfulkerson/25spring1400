# What would the output of the following code be if the input was 13?

things = [81, 8123, 12, -87, 7671, -4351]
search = int(input("Favorite number? "))
if search > max(things) or search < min(things):
    print("Abracadabra")
else:
    print("Hocus Pocus")

