my_list = [1, 2, 3]
print("Original List:", my_list)

my_list.append(4)
print("After append(4):", my_list)

my_list.extend([5, 6])
print("After extend([5, 6]):", my_list)

my_list.insert(1, 100)
print("After insert(1, 100):", my_list)

my_list.remove(3)
print("After remove(3):", my_list)

last_item = my_list.pop()
print("After pop():", my_list)
print("Popped item:", last_item)

del my_list[0]
print("After del my_list[0]:", my_list)

print("Final List:", my_list)
