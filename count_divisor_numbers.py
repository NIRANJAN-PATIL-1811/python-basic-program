# Write a Python program to find the total number of even or odd divisors of a given integer.

user_input = int(input("Enter a integer number: "))

print("Divisor(s) are below!")
for i in range(1,user_input+1):
    if user_input % i == 0:
        print(i)