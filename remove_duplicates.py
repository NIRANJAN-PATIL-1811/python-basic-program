def remove_duplicates(nums):
    if not nums:
        return 0

    # Sort the array to group duplicates together
    nums.sort()

    # Initialize variables
    unique_count = 1
    current_num = nums[0]

    # Iterate through the array and remove duplicates
    for num in nums[1:]:
        if num != current_num:
            current_num = num
            unique_count += 1

    return unique_count

# Example usage:
input_array = [1, 2, 3, 4, 4, 5, 6, 6, 7]
new_length = remove_duplicates(input_array)

print(f"Original Array: {input_array}")
print(f"Array after removing duplicates: {input_array[:new_length]}")
print(f"New Length: {new_length}")
