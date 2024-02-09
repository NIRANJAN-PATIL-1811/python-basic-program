class Get_factorial:
    def fact(self, user_input):
        if user_input == 1 or user_input == 1:
            return user_input
        
        return user_input * self.fact(user_input - 1)
    

print(Get_factorial().fact(5))