set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

print("\nUnion:", set1 | set2)  

print("Intersection:", set1 & set2)  

print("Difference (set1 - set2):", set1 - set2)  

print("Symmetric Difference:", set1 ^ set2)  

print("Is set1 subset of set2?", set1.issubset(set2))

print("Is set1 superset of set2?", set1.issuperset(set2))

print("Are sets disjoint?", set1.isdisjoint(set2))
