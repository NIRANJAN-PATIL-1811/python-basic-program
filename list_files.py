#  Write a Python program to find files and skip directories in a given directory.

import os

user_path = str(input("Enter the path: "))
os.system(f"ls -f {user_path}")