# highlights from lecture 10

a = float(input("Enter a grade: "))
b = float(input("Enter a grade: "))
c = float(input("Enter a grade: "))
d = float(input("Enter a grade: "))

drop = 0
if a <= b and a <= c and a <= d:
    drop = a
elif b <= a and b <= c and b <= d:
    drop = b
elif c <= a and c <= b and c <= d:
    drop = c
else:
    drop = d

smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c
if d < smallest:
    smallest = d

the_smallest = min(a, b, c, d)

print(drop, smallest, the_smallest)

print(f"Your lowest quiz score was {drop:.2f}")

average = (a + b + c + d - drop) / 3

print(f"Your quiz average is: {average:.2f}")

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
    
print(f"Your course grade is {grade}")
