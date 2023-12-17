# Write a Python program to find the number of zeros at the end of a factorial of a given positive number. 

user_input = int(input("Enter a number: "))


def rec(val):
    i = 1
    ans = 1
    while i <= val:
        ans = ans * i
        i = i + 1
    ans2 = str(ans)

    starting_point = len(ans2)
    ending_point = 0

    final_ans = 0

    while starting_point > ending_point:
        if ans2[int(starting_point - 1)] == '0':
            final_ans = final_ans + 1
            starting_point = starting_point - 1
        elif ans2[int(starting_point - 1)] != '0':
            break
        else:
            starting_point = starting_point - 1
    return final_ans

x = rec(user_input)
print(x)