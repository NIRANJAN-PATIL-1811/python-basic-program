def running_product(iterable):
    result = []
    product = 1
    for num in iterable:
        product *= num
        result.append(product)
    return result

# Example usage:
numbers = [1, 2, 3, 4, 5]
print("Running product of", numbers, ":", running_product(numbers))
