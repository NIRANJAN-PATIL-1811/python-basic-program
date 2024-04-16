def find_smallest_multiple(n):
    # Initialize result
    result = 1

    # Find the LCM of numbers from 1 to n
    for i in range(1, n + 1):
        result = (result * i)//(gcd(result, i))
    return result

# Function to calculate gcd of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to display factors of a number
def display_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# Main program
n = int(input("Enter the value of n: "))
smallest_multiple = find_smallest_multiple(n)
print("The smallest multiple of the first", n, "numbers is:", smallest_multiple)
print("Factors of", smallest_multiple, "are:", display_factors(smallest_multiple))
