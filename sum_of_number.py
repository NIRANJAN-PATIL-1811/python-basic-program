class Sum:
    def getFirstAndSecondInput(self):
        # get first input from user
        self.first_input = int(input("Enter starting number: "))

        # get second input from user
        self.second_input = int(input("Enter second number: "))

    def returnAns(self):
        finalAns_1 = (self.first_input) * (self.first_input + 1) / 2
        finalAns_2 = (self.second_input) * (self.second_input + 1) / 2

        finalAns = finalAns_2 - finalAns_1

        return finalAns

obj = Sum()
obj.getFirstAndSecondInput()

print(f"The Sum of difference between {obj.first_input} and {obj.second_input} is = {obj.returnAns()}")