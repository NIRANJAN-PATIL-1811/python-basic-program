import re

def match_pattern(string):
    pattern = r'a+b+'
    match = re.match(pattern, string)
    if match:
        return True
    else:
        return False

# Test the function
test_strings = ["ab", "abb", "aabb", "abc", "ac", "aab", "bb"]
for test_string in test_strings:
    print(f"String '{test_string}': Matched? {match_pattern(test_string)}")
