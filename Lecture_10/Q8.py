x = int(input("Enter a number: "))

if x > 10:
    result = "High"
else:
    result = "Low"

print(result)

# result = "Low" if x < 10 else "High"    # Option A
# result = "High" if x > 10 else "Low"    # Option B
# result = "High" if x < 10 else "Low"    # Option C
# result = "Low" if x > 10 else "High"    # Option D

print("""
x	if/else		A	B	C	D
9 	Low		Low	Low	High	High
10 	Low		High	Low	Low	High
11 	High		High	High	Low	Low
""")

