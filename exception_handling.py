def perform_division(dividend, divisor):
    try:
        result = dividend / divisor
        print(f"The result of {dividend} / {divisor} is: {result}")
    except ArithmeticError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
try:
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
    perform_division(dividend, divisor)
except ValueError:
    print("Error: Please enter valid numeric values for dividend and divisor.")
