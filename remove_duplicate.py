def remove_duplicates(input_list):
    unique_list = []
    
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    
    return unique_list

# Example usage:
input_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 9, 1]
result = remove_duplicates(input_list)

print("Original List:", input_list)
print("List with Duplicates Removed:", result)
