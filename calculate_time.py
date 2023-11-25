# Write a Python program to calculate the time runs (difference between start and current time) of a program.

import time

x = time.time()

for i in range(10000000):
    print(i)

y = time.time()


z = y - x
print(f"Time taken is = {z} sec.")