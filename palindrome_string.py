class Palindrome:
    def reverse(self, __string):
        return_string = ''
        for string in __string[::-1]:
            return_string = return_string + string
        return return_string
    

user_input = input("Enter your string: ")


if Palindrome().reverse(user_input) == user_input:
    print("Given string is a Palindrome string")
else:
    print("Given string is not a Palindrome string")