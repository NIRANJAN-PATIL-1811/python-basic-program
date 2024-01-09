def reverse_vowels(input_str):
    vowels = "aeiouAEIOU"
    input_list = list(input_str)
    left, right = 0, len(input_list) - 1

    while left < right:
        while left < right and input_list[left].lower() not in vowels:
            left += 1

        while left < right and input_list[right].lower() not in vowels:
            right -= 1

        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1
        right -= 1

    return ''.join(input_list)

# Example usage:
input_string = "Hello World"
result = reverse_vowels(input_string)
print("Original String:", input_string)
print("String with reversed vowels:", result)
