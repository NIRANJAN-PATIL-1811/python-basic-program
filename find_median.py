def find_median(num1, num2, num3):
    # Arrange the numbers in ascending order
    numbers = [num1, num2, num3]
    numbers.sort()

    # The median is the middle element in a sorted list
    median = numbers[1]
    return median

# Example usage
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

median = find_median(num1, num2, num3)

print(f"The median among {num1}, {num2}, and {num3} is: {median}")
