# Write a Python program to retrieve the path and name of the file currently being executed.

import os
x = os.path.realpath(__file__)
print(x)