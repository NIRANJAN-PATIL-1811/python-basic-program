user_input = int(input("Enter a number: "))

if user_input >= 0 and user_input <= 100:
    print(f"{user_input} is within 0 - 100")
elif user_input >= 101 and user_input <= 1000:
    print(f"{user_input} is within 101 - 1000")
elif user_input >= 1001 and user_input <= 2000:
    print(f"{user_input} is within 1001 - 2000")
else:
    print(f"{user_input} is out of 2001")