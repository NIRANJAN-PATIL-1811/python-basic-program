def max_product_pair(numbers):
    # Convert list to set to remove duplicates
    num_set = set(numbers)
    
    # Sort the set
    sorted_nums = sorted(num_set)
    
    # If there are less than two numbers, return None
    if len(sorted_nums) < 2:
        return None
    
    # Get the largest and second largest numbers
    largest = sorted_nums[-1]
    second_largest = sorted_nums[-2]
    
    # Get the smallest and second smallest numbers
    smallest = sorted_nums[0]
    second_smallest = sorted_nums[1]
    
    # Calculate products
    product1 = largest * second_largest
    product2 = smallest * second_smallest
    
    # Compare products and return the pair with the maximum product
    if product1 > product2:
        return (largest, second_largest)
    else:
        return (smallest, second_smallest)

# Example usage
numbers = [1, 10, 3, -1, -20, 30, 2]
result = max_product_pair(numbers)
print(f"The pair with the maximum product is: {result}")
