# List of tuples
list_of_tuples = [(1, 5), (3, 2), (2, 8), (4, 1)]

# Sort the list of tuples based on the second element of each tuple
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])

print("Sorted list of tuples:", sorted_list)
