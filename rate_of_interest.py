amount = int(input("Enter the number of amount: "))
interest = float(input("Enter the number of interest: "))
duration = float(input("Enter the number of duration: "))

final_ans = (amount * interest * duration) / 100
print(amount + final_ans)