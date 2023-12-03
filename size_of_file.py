# Write a Python program to get the size of a file.

import os

sample_path = "/home/roshan/python/bms.py"

print(f"{os.path.getsize(sample_path)} bytes.")