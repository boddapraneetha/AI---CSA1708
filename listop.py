# 1. Nested List
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Nested List:", nested_list)

# 2. Length of a List
print("Length of nested_list:", len(nested_list))

# 3. List Concatenation
list1 = [10, 20, 30]
list2 = [40, 50]
combined = list1 + list2
print("Concatenated List:", combined)

# 4. Membership Test
print("Is 20 in list1?", 20 in list1)
print("Is 99 in list2?", 99 in list2)

# 5. Iteration
print("Iterating over combined list:")
for item in combined:
    print(item, end=' ')
print()

# 6. Indexing
print("First element of list1:", list1[0])
print("Last element of list2:", list2[-1])

# 7. Slicing
print("First two elements of combined list:", combined[:2])
print("Elements from index 2 to 4:", combined[2:5])
print("All except last item:", combined[:-1])
