def find_indices(lst, item):
    indices = [index for index, value in enumerate(lst) if value == item]
    return indices

# Example usage
my_list = [1, 2, 3, 2, 4, 2, 5, 2]
search_item = 2

result = find_indices(my_list, search_item)

if result:
    print(f"The item {search_item} is found at indices: {result}")
else:
    print(f"The item {search_item} is not found in the list.")
