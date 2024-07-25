import math

def main():
    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate cube root of the first number
    cube_root_num1 = math.pow(num1, 1/3)

    # Calculate square root of the second number
    sqrt_num2 = math.sqrt(num2)

    # Check if the cube root of the first number is equal to the square root of the second number
    if cube_root_num1 == sqrt_num2:
        print("The cube root of", num1, "is equal to the square root of", num2)
    else:
        print("The cube root of", num1, "is not equal to the square root of", num2)

if __name__ == "__main__":
    main()

