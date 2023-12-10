# Write a Python program to find out three numbers from given list who's sum is 9.

target_no = 9

sample_list = [5,3,2,5,1,4]

def myfun(sample_list, target_no):
    for i in range(len(sample_list)):
        for j in range((i + 1), len(sample_list)):
            for l in range((i + 2), len(sample_list)):
                if sample_list[i] + sample_list[j] + sample_list[l] == target_no:
                    return sample_list[i], sample_list[j], sample_list[l]
            

x = myfun(sample_list, target_no)
print(x)