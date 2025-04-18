s = input()
#s = s.split()
f = {}

for a in s:
    if a in f:
        f[a] += 1
    else:
        f[a] = 1

# for a in s:
#    if len(a) in f:
#        f[len(a)] += 1
#    else:
#        f[len(a)] = 1