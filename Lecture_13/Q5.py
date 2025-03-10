# What is printed from the following code?

set1 = set(['a','b','c'])
set2 = {'b','c','d'}
set3 = set(['c','d','e'])
# sorted() is a valid method, returns values in ascending order
print(sorted(set1.intersection(set2)), end=' ')
print(sorted(set1.difference(set2, set3)))

print(sorted(set1 - set2 - set3))

print(sorted(set1.union(set2)))

