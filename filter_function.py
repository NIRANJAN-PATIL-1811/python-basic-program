def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter_even_numbers(numbers)
print(filtered_numbers)
