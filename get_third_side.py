# Write a Python program to get the third side of a right-angled triangle from two given sides.

import math
print("Note:  There are three sides 1.AB, 2.Bc and 3.AC")
user_input1 = float(input("Enter the value for side AB: "))
user_input2 = float(input("Enter the value for side BC: "))

AC = user_input1**2 + user_input2**2

ans = math.sqrt(AC)
print(f"AC = {ans}")