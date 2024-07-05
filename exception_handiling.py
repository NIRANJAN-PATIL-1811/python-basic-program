def get_valid_integer():
    while True:
        try:
            user_input = input("Enter an integer: ")
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage
try:
    result = get_valid_integer()
    print("You entered:", result)
except ValueError as ve:
    print(f"Error: {ve}")
