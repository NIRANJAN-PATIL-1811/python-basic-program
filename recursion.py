def recursive_sum(numbers):
    # Base case: if the list is empty, return 0
    if not numbers:
        return 0
    # Recursive case: sum the first element with the sum of the rest of the list
    else:
        return numbers[0] + recursive_sum(numbers[1:])

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = recursive_sum(my_list)
print(f"The sum of the list {my_list} is: {result}")
