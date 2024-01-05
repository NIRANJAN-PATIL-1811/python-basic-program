def replace_strings(input_string):
    # Replace "Python" with a temporary placeholder
    temp_placeholder = "###TEMP_PLACEHOLDER###"
    modified_string = input_string.replace("Python", temp_placeholder)

    # Replace "Java" with "Python"
    modified_string = modified_string.replace("Java", "Python")

    # Replace the temporary placeholder with "Java"
    modified_string = modified_string.replace(temp_placeholder, "Java")

    return modified_string

if __name__ == "__main__":
    input_string = "I love Python programming. Java is also a great language."

    modified_string = replace_strings(input_string)

    print("Original String:")
    print(input_string)

    print("\nModified String:")
    print(modified_string)
