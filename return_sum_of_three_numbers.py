first_value = int(input("Enter first value: "))
second_value = int(input("Enter second value: "))
third_value = int(input("Enter third value: "))

def myfun(value):
    return value + value + value

if first_value == second_value == third_value:
    for i in range(3):
        x = myfun(first_value)
        print(x)
else:
    sum = first_value + second_value + third_value
    print(sum)
