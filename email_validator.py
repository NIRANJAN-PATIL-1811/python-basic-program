class Email_Validator:
    def validiate(self, email):
        val = email[-10:]

        if val == "@gmail.com":
            return "Email is Valid!"
        else:
            return "Email is Not Valid!"


result = Email_Validator().validiate("rosh.rp1811@gmail.com")
print(result)