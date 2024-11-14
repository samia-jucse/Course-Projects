my_list = [3]  # '3' is referenced by the list at some memory location (id).
print(id(my_list))  # Let's say: 140493857877456
print(id(my_list[0]))  # Let's say: 9793152 (memory location for the integer 3)

# Modify the list
my_list[0] = 4  # The reference to 3 is replaced with a reference to 4
print(my_list)  # Output: [4]
print(id(my_list))  # Same id as before: 140493857877456
print(id(my_list[0]))  # New id for 4: 9793184
