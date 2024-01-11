def find_largest_and_smallest_digits(number):
    # Convert the number to a string to iterate through its digits
    number_str = str(number)

    # Initialize variables to store the largest and smallest digits
    largest_digit = smallest_digit = int(number_str[0])

    # Iterate through the digits of the number
    for digit_char in number_str:
        digit = int(digit_char)

        # Update the largest digit if the current digit is larger
        if digit > largest_digit:
            largest_digit = digit

        # Update the smallest digit if the current digit is smaller
        if digit < smallest_digit:
            smallest_digit = digit

    return largest_digit, smallest_digit

# Get user input for the number
number = int(input("Enter a number: "))

# Call the function and print the results
largest, smallest = find_largest_and_smallest_digits(number)
print(f"Largest digit: {largest}")
print(f"Smallest digit: {smallest}")
