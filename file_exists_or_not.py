import os.path

user_file_path = input("Enter your file path: ")

if os.path.isfile(user_file_path):
    print("File Exists!")
else:
    print("File does not Exists!")