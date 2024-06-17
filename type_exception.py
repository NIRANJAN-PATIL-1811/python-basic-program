def get_numerical_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a numerical value.")

def main():
    try:
        num1 = get_numerical_input("Enter the first number: ")
        num2 = get_numerical_input("Enter the second number: ")
        result = num1 + num2
        print("The sum of the numbers is:", result)
    except TypeError:
        print("TypeError: Inputs must be numerical.")

if __name__ == "__main__":
    main()
