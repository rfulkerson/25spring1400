# Find and output all Pythagorean triples where a, b, and c range from 1 through 5.

# Remember that a Pythagorean triple satisfies the condition:𝑎^2+𝑏^2=𝑐^2

# How could you modify the code to test larger ranges?
# Modify the code to test ranges based on user input.

import time

start = time.perf_counter()

print("Finding Pythagorean Triples!")

count = 0
for a in range(1,501):
    for b in range(1,501):
        for c in range(1,501):
            if a**2 + b**2 == c**2:
                count += 1
                print(a,b,c)

end = time.perf_counter()

print("Done!")
print(f'It took {end-start:.2f} seconds to identify all {count} pythagorean triples.')
