first_value = int(input("Enter first value: "))
second_value = int(input("Enter second value: "))
third_value = int(input("Enter third value: "))

sum = 0

if first_value == second_value or second_value == third_value:
    sum = 0
else:
    sum = first_value + second_value + third_value

print(sum)