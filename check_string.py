def are_letters_present(first_string, second_string):
    # Convert both strings to lowercase for case-insensitive comparison
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Check if each letter in the second string is present in the first string
    for char in second_string:
        if char.isalpha() and char not in first_string:
            return False

    return True

# Get input from the user
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

# Check if letters in the second string are present in the first string
result = are_letters_present(first_string, second_string)

# Display the result
if result:
    print("All letters in the second string are present in the first string.")
else:
    print("Not all letters in the second string are present in the first string.")
