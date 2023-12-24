#  Write a Python program to check whether lowercase letters exist in a string.


name = "HELLo"

for i in range(len(name)):
    if name[i].islower():
        print("Present!")
        break
    else:
        pass