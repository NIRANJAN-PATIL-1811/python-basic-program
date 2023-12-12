# Write a Python program to find common divisors between two numbers.

user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))

user_input1_list = []
user_input2_list = []

for i in range(1, user_input1 + 1):
    if user_input1 % i == 0:
        user_input1_list.append(i)


for i in range(1, user_input2 + 1):
    if user_input2 % i == 0:
        user_input2_list.append(i)


a = set(user_input1_list)
b = set(user_input2_list)

result = a.intersection(b)
if result:
    print(result)
else:
    print("Nothing!")