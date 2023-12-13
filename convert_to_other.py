# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

user_input = float(input("Enter the distance in feet: "))

inches = user_input * 12
print(f"{inches} inch.")


yard = user_input * 0.33333
print(f"{yard} yard.")


miles = user_input * 0.000189394
print(f"{miles} miles.")