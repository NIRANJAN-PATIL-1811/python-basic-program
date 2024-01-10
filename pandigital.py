def is_pandigital_number(num):
    num_str = str(num)
    n = len(num_str)
    
    # Check if the length of the number is equal to the number of unique digits
    if n != len(set(num_str)):
        return False
    
    # Check if the number contains all digits from 1 to n
    for i in range(1, n + 1):
        if str(i) not in num_str:
            return False
    
    return True

# Example usage:
user_input = int(input("Enter an integer to check for pandigitality: "))

if is_pandigital_number(user_input):
    print(f"{user_input} is a Pandigital number.")
else:
    print(f"{user_input} is not a Pandigital number.")
