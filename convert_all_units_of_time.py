# Write a Python program to convert all units of time into seconds. 

user_input = int(input("Enter no of minutes: "))

seconds = 60 * user_input
print(f"{seconds} seconds")


print(f"{user_input} minutes")


hours = user_input / 60
print(f"{hours} hours")



day = (user_input / 60 ) / 24
print(f"{day} day")