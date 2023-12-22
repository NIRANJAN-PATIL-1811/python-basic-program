# Write a Python program that accepts a positive number and subtracts from it the sum of its digits, and so on. Continue this operation until the number is positive.

user_input1 = str(input("Enter a number: "))
user_input = int(user_input1)
rotation = 0

while rotation < user_input:
    sum = 0
    for i in range(len(str(user_input))):
        sum = sum + int(str(user_input)[i])
    ans = user_input - sum
    if ans == 0:
        break
    else:
        print(user_input - sum)
    user_input = user_input - 1