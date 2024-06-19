def count_occurrences(arr, element):
    return arr.count(element)

# Example usage:
my_array = [1, 2, 3, 4, 2, 2, 5, 6, 2]
specified_element = 2

occurrences = count_occurrences(my_array, specified_element)

print(f"The number of occurrences of {specified_element} in the array is: {occurrences}")
