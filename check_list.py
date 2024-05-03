def is_empty(input_list):
    return not bool(input_list)

# Test the function
test_list = []
print(is_empty(test_list))  # Output: True

test_list = [1, 2, 3]
print(is_empty(test_list))  # Output: False
