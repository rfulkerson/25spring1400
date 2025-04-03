# find pythagorean triples

import time

howmany = 0
max_value = 250

start = time.perf_counter()

for a in range(1,max_value):
    for b in range(1,max_value):
        for c in range(1,max_value):
            if a**2 + b**2 == c**2:
                print(a,b,c)
                #howmany += 1
                
end = time.perf_counter()

print(f"I just tested {max_value**3} possibilities.")
print(f"There were {howmany} pythag triples")
print(f"It took me {end-start:.2f} seconds to do that!")

