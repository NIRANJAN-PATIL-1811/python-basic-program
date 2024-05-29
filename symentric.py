# Function to find the symmetric difference of two sets
def symmetric_difference(set1, set2):
    # Using the ^ operator to get the symmetric difference
    return set1 ^ set2

# Example usage
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = symmetric_difference(set1, set2)
print("Symmetric Difference using ^ operator:", result)

# Another way to find the symmetric difference using symmetric_difference() method
result_method = set1.symmetric_difference(set2)
print("Symmetric Difference using symmetric_difference() method:", result_method)
