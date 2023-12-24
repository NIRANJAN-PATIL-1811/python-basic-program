# Write a Python program to find the digits that are missing from a given mobile number.

user_input = input("Enter your mobile number: ")

for i in range(len(user_input)):
    if str(i) not in user_input:
        print(f"Missing {str(i)}")