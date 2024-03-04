def sort_list_of_dicts(list_of_dicts, key_to_sort):
    """
    Sort a list of dictionaries based on the values of a specified key.

    Parameters:
    - list_of_dicts (list): List of dictionaries to be sorted.
    - key_to_sort (str): Key based on which the dictionaries should be sorted.

    Returns:
    - list: Sorted list of dictionaries.
    """
    return sorted(list_of_dicts, key=lambda x: x[key_to_sort])

# Example usage:
list_of_dicts = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_list = sort_list_of_dicts(list_of_dicts, key_to_sort='age')
print(sorted_list)
