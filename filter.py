def filter_strings_with_substring(strings, substring):
    filtered_strings = filter(lambda x: substring not in x, strings)
    return list(filtered_strings)

# Example usage:
strings_list = ["apple", "banana", "orange", "grape", "pineapple"]
substring = "an"
filtered_list = filter_strings_with_substring(strings_list, substring)
print(filtered_list)
