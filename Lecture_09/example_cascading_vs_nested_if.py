x = float(input("Please enter a value: "))
y = int(input("Enter another number: "))

# demonstrating cascading and nested if/else structures.

# cascading if/elif/elif/else
if x > 100.5:
    print("This is a big value!")
elif x > 50.25:
    # this is the nested if/else as the action of the first elif of the
    # cascading if/elif/elif/else
    if y == 7:
        print("You found the 7!")
    else:
        print("Your value of y didn't find the magic output")
    print("This is a middling value!")
elif x > 0.00:
    print("At least we weren't negative!")
else:
    print("That's a negative value!")