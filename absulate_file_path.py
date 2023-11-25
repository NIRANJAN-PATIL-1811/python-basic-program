# Write a Python program to get an absolute file path.

import os

try:
    x = os.path.abspath("file_name.txt")
    print(x)
except:
    print("Path does not exist!")