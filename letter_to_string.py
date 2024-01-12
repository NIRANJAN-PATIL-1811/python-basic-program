def sort_letters(input_str):
    # Convert the input string to lowercase
    lower_str = input_str.lower()

    # Convert the string to a list of characters, sort them, and join back into a string
    sorted_str = ''.join(sorted(lower_str))

    return sorted_str

# Get input from the user
user_input = input("Enter a string: ")

# Call the function and print the result
result = sort_letters(user_input)
print("Sorted string:", result)
