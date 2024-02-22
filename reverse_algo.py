sample_list = [76,4,7,4,6,3,65]

first = sample_list[0]
second = sample_list[1]

new_list = []

for i in sample_list[2:]:
    new_list.append(i)
new_list.append(first)
new_list.append(second)
print(new_list)