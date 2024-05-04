# List of tuples
tuples_list = [('John', 25), ('Alice', 20), ('Bob', 30), ('Jane', 22)]

# Sorting the list of tuples based on the second element of each tuple (age)
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Displaying the sorted list
print("Sorted list of tuples based on the second element (age):")
print(sorted_list)
