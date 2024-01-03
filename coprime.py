def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(num1, num2):
    return gcd(num1, num2) == 1

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = are_coprime(num1, num2)

if result:
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are not coprime.")
