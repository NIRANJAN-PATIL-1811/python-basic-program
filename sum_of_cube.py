# Write a Python function that takes a positive integer and returns the sum of the cube.

user_input1 = int(input("Enter a number: "))
user_input2 = int(input("Enter a number of cube: "))

def cub(num1, num2):
    if num1 == 0:
        return 0
    else:
        x = 1
        for i in range(num2):
            x = x * num1
        return x



x = cub(user_input1, user_input2)

print(f"The sum is = {x}")