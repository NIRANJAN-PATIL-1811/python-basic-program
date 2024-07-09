def count_equal_numbers(num1, num2, num3):
    equal_count = 0

    if num1 == num2 == num3:
        equal_count = 3
    elif num1 == num2 or num1 == num3 or num2 == num3:
        equal_count = 2

    return equal_count

# Input three integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Count equal numbers
result = count_equal_numbers(num1, num2, num3)

# Display the result
if result == 0:
    print("No equal numbers.")
elif result == 1:
    print("One pair of equal numbers.")
elif result == 2:
    print("Two pairs of equal numbers.")
elif result == 3:
    print("All three numbers are equal.")
