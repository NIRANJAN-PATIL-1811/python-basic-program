sample_file = input("Enter your file name:")

deliminator = sample_file.find('.')

print(sample_file[deliminator+1:])