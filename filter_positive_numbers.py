#  Write a Python program to filter positive numbers from a list.

sample_list = [-3,5,-4,-6,3,-9,2]

new_list = []


for i in range(len(sample_list)):
    if sample_list[i] >= 0:
        new_list.append(sample_list[i])



print(new_list)