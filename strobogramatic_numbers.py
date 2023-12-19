# Get all strobogrammatic numbers that are of length 999.

sample_list = ['1', '6', '8', '9', '0']

final_list = []

for i in range(1000):
    i2 = str(i)
    if len(i2) == 1:
        if i2 == '0' or i2 == '1' or i2 == '8':
            final_list.append(i2)
    if len(i2) == 2:
        if (i2[0] == '1' and i2[1] == '1') or (i2[0] == '8' and i2[1] == '8') or (i2[0] == '6' and i2[1] == '9') or (i2[0] == '9' and i2[1] == '6'):
            final_list.append(i2)
    if len(i2) == 3:
        if (i2[0] == '6') and (i2[2] == '9') and (i2[1] == '1' or i2[1] == '8' or i2[1] == '0'):
            final_list.append(i2)
        if (i2[0] == '9') and (i2[2] == '6') and (i2[1] == '1' or i2[1] == '8' or i2[1] == '0'):
            final_list.append(i2)
        if (i2[0] == '1') and (i2[2] == '1') and (i2[1] == '1' or i2[1] == '8' or i2[1] == '0'):
            final_list.append(i2)
        if (i2[0] == '8') and (i2[2] == '8') and (i2[1] == '1' or i2[1] == '8' or i2[1] == '0'):
            final_list.append(i2)
print(final_list)