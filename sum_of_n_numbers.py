#  Write a Python program to sum the first n positive integers.

user_input = int(input("Enter the number first n positive integer number: "))

x = 0
i = 0
while i != user_input + 1:
    x = x + i
    i = i + 1


print(f"The sum is = {x}")