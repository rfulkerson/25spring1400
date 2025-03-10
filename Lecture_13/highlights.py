# Given the following two sets of friends, find:

# All the friends (union)
# The friends that are common to both groups (intersection)
# The friends only in group_1 (difference)
# The friends only in group_2 (difference)
# The friends unique to both groups (symmetric_difference)

group_1 = {"Nichole", "Tyreese", "Mustafa", "Aliza"}
group_2 = {"Aliza", "Nichole", "Judah", "Toby", "Vikki"}
print(group_1)
print(group_2)
print()

# All the friends (union)
all_friends = group_1.union(group_2)
print("Union:", all_friends)
print()

# The friends that are common to both groups (intersection)
in_both_groups = group_1.intersection(group_2)
print("Intersection:", in_both_groups)
print()

# The friends only in group_1 (difference)
only_in_g1 = group_1.difference(group_2)
print("Only in G1:", only_in_g1)
print()

# The friends only in group_2 (difference)
only_in_g2 = group_2.difference(group_1)
print("Only in G2:", only_in_g2)
print()

# The friends unique to both groups (symmetric_difference)
in_g1_or_g2 = group_2.symmetric_difference(group_1)
print("Unique to G1 or G2:", in_g1_or_g2)
print()

# All of the friends, minus the overlapping friends
other = group_2.union(group_1).difference(group_2.intersection(group_1))
print("All friends minus common friends:", other)
print()

