# Write a Python program to check whether a file path is a file or a directory.

# sample_path = input("Enter file path: ")

import os

sample_path1  = "/home/John/python"

if os.path.isdir(sample_path1) == True:
    print("True!")
else:
    print("False!")