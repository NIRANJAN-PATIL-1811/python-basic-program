def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]
        return last_n_lines

file_path = "example.txt"  # Replace 'example.txt' with the path to your file
n = 5  # Number of lines to read from the end

try:
    last_n_lines = read_last_n_lines(file_path, n)
    for line in last_n_lines:
        print(line, end='')
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
