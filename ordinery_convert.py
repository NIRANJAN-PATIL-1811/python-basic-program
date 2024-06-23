import array

def convert_array_to_list(arr):
    return arr.tolist()

# Example usage:
arr = array.array('i', [1, 2, 3, 4, 5])
ordinary_list = convert_array_to_list(arr)
print(ordinary_list)
