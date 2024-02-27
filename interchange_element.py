sample_list = [1,2,3,4,5,6,7,8]


def fun(sample_list):
    sample_list[0], sample_list[-1] = sample_list[-1], sample_list[0]
    return sample_list
print(fun(sample_list))