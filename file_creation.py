# Write a Python program that retrieves the date and time of file creation and modification.

import os.path, time

file_path = "os_info.py"

print("Last modified time %s" % time.ctime(os.path.getmtime(file_path)))
print("Creation time %s" % time.ctime(os.path.getctime(file_path)))