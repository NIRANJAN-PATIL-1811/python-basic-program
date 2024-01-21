def compute_sum(arr):
    # Initialize sums for positive and negative numbers
    sum_positive = 0
    sum_negative = 0

    # Iterate through the array
    for num in arr:
        if num > 0:
            sum_positive += num
        elif num < 0:
            sum_negative += num

    # Find the largest sum
    largest_sum = max(sum_positive, sum_negative)

    return largest_sum

# Example usage:
input_array = [3, -7, 2, -9, 5, 1, -8]

result = compute_sum(input_array)

print("The largest sum is:", result)
