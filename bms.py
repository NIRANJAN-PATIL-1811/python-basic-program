#  Write a Python program to calculate the body mass index.

user_input1 = float(input("Enter your height in feet: "))
user_input2 = float(input("Enter your weight in kg: "))

user_height_meter = user_input1 * 0.3048

BMI = user_input2 / (user_height_meter * user_height_meter)

print(f"Your BMI = {BMI}")