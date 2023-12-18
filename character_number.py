# Write a Python program to count the number of occurrences of a specific character in a string.

sample_string = "John loves to sleep"

sample_char = "s"
no_of_char = 0

for i in range(len(sample_string)):
    if sample_string[i] == sample_char:
        no_of_char = no_of_char + 1

print(no_of_char)