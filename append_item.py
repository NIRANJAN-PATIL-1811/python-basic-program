def append_to_array(arr, iterable):
    """
    Appends items from iterable to the end of the array.

    Parameters:
    - arr: The array to which items will be appended.
    - iterable: The iterable containing items to be appended.

    Returns:
    None
    """
    arr.extend(iterable)

# Example usage:
my_array = [1, 2, 3, 4]
my_iterable = [5, 6, 7, 8]

append_to_array(my_array, my_iterable)

print("Updated array:", my_array)
