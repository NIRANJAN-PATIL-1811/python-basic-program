list1 = ["white", "black", "red"]
list2 = ["red","green"]

for i in range(len(list1)):
    if list1[i] not in list2:
        print(list1[i])
    else:
        pass