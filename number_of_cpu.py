#  Write a Python program to find out the number of CPUs used.

import multiprocessing
x = multiprocessing.cpu_count()
print(x)