sample_list = ["apple", "bannana", "mango", "greps"]

new_list = []

for word in sample_list:
    myword = ""
    for i in word[::-1]:
        myword = myword + i
    new_list.append(myword)
    # print()

print(new_list)