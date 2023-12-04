# Write a Python program to sort files by date.

import os
import glob

file = glob.glob("*.py")
file.sort(key=os.path.getmtime)
print("\n",file)