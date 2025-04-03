# find pythagorean triples

import time
import math

howmany = 0
max_value = 200

start = time.perf_counter()

for a in range(1,max_value):
    for b in range(1,max_value):
        for c in range(1,max_value):
            if a**2 + b**2 == c**2:
                print(a,b,c)
                howmany += 1
                
end = time.perf_counter()

print("Using a**2 + b**2 == c**2:")
print(f"I just tested {max_value**3} possibilities.")
print(f"There were {howmany} pythag triples")
print(f"It took me {end-start:.2f} seconds to do that!")

input("Hit enter to continue")

#####################################################################

def triple(a,b,c):
    return a**2 + b**2 == c**2
    
howmany = 0
start = time.perf_counter()

for a in range(1,max_value):
    for b in range(1,max_value):
        for c in range(1,max_value):
            if triple(a,b,c):
                print(a,b,c)
                howmany += 1

end = time.perf_counter()

print("Using triple(a,b,c) with ** in the function:")
print(f"I just tested {max_value**3} possibilities.")
print(f"There were {howmany} pythag triples")
print(f"It took me {end-start:.2f} seconds to do that!")

input("Hit enter to continue")


#####################################################################
start = time.perf_counter()
howmany = 0

for a in range(1,max_value):
    for b in range(1,max_value):
        for c in range(1,max_value):
            if math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
                print(a,b,c)
                howmany += 1
                
end = time.perf_counter()

print("Using math.pow(a,2) + math.pow(b,2) == math.pow(c,2):")
print(f"I just tested {max_value**3} possibilities.")
print(f"There were {howmany} pythag triples")
print(f"It took me {end-start:.2f} seconds to do that!")

input("Hit enter to continue")

#####################################################################

def triplemathpow(a,b,c):
    return math.pow(a,2) + math.pow(b,2) == math.pow(c,2)

start = time.perf_counter()
howmany = 0

for a in range(1,max_value):
    for b in range(1,max_value):
        for c in range(1,max_value):
            if triplemathpow(a,b,c):
                print(a,b,c)
                howmany += 1
                
end = time.perf_counter()

print("Using triplemathpow(a,b,c) with math.pow() in the function:")
print(f"I just tested {max_value**3} possibilities.")
print(f"There were {howmany} pythag triples")
print(f"It took me {end-start:.2f} seconds to do that!")

