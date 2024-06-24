# Pograme to check if a string is same or not even if it is reversed.

def checkString(string):
    newstring = list(string)
    i_start = 0
    j_start = len(newstring) - 1
    while i_start != j_start:
        if (newstring[i_start] != newstring[j_start]):
            return False
        else:
            i_start = i_start + 1
            j_start = j_start - 1
    return True

print(checkString("madam"))