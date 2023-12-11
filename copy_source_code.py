# Write a Python program to create a copy of its own source code.

file = open("/home/John/python/copy_source_code.py", "r+")
x = file.read()

file2 = open("/home/John/python/copy_source_code2.py", "w")
file2.write(x)

print("Done!")