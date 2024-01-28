# Create a guessing number game

import random

computer_generated_number = random.randint(1, 10)

print(computer_generated_number)

def guess_number(val):
	if computer_generated_number == val:
		return True
	else:
		return False
	
i = True

while i != False:
	user_input = int(input("You: "))
	if guess_number(user_input) == True:
		print("Your choice is correct! Thank You!!")
		i = False
	elif computer_generated_number <= user_input:
		print("Choose lasser!")
	elif computer_generated_number >= user_input:
		print("Choose bigger!")
	else:
		pass