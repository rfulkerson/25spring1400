temp = 85
humidity = 20
wind = 5

if temp > 80 or humidity < 10 and wind > 10:
    print("Pickleball!")
elif temp > 60 and humidity < 50 or wind < 15:
    print("Frisbee!")
else:
    print("Let's read!")
