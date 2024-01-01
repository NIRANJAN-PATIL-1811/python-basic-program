def is_palindrome(num):
    # Convert the integer to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Input a number from the user
user_input = input("Enter an integer: ")

try:
    # Convert the user input to an integer
    user_number = int(user_input)
    
    # Check if the number is a palindrome
    if is_palindrome(user_number):
        print(f"{user_number} is a palindrome!")
    else:
        print(f"{user_number} is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
