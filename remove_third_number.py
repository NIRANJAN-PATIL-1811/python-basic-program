# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

sample_list = [56,43,5,2,54,13,9,7,645,86,46,97,46,9,6,44,74,97,46,86,53,84,83,35,64,37,37,28]

i = 3

while i < len(sample_list):
    print(sample_list[i])
    sample_list.remove(sample_list[i])
    i = i + 2