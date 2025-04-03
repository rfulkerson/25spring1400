# finding pythagorean triples

count = 0
for a in range(1,501):       # 1 through 5
    #print(a)
    for b in range(1,501):   # 1 through 5
        #print(a,b)
        for c in range(1,501): # 1 through 5
            #print(a,b,c)
            if a**2 + b**2 == c**2:
                print(a,b,c)
                count += 1
print(f"found {count} triples")
    