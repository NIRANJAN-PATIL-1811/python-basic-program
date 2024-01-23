def has_consecutive_letters(input_str):
    for i in range(len(input_str) - 1):
        if input_str[i] == input_str[i + 1]:
            return True
    return False

# Example usage:
user_input = input("Enter a string: ")
if has_consecutive_letters(user_input):
    print("The string contains two similar consecutive letters.")
else:
    print("The string does not contain two similar consecutive letters.")
