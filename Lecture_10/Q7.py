
x = int(input("Enter a number for x: "))

if x > 10:
    result = "High"
else:
    result = "Low"

print(result)

print
print ("""
X	if/else	A	B	C	D
9 	Low	Low	Low	High	High
10 	Low	High	Low	Low	High
11 	High	High	High	Low	Low
""")