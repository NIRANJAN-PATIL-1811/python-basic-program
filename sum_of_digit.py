#  Write a Python program to calculate sum of digits of a number.

user_input = input("Enter a number: ")

x = map(int, user_input)

mylist = list(x)

sum = 0

for i in range(len(mylist)):
    sum = sum + mylist[i]

print(f"Sum = {sum}")