#  Write a Python program to validate an IP address.

# user_ip = str(input("Enter the IP: "))
user_ip = "192.164.0.100"

for i in range(1):
    x = user_ip.split(".")
    for j in range(len(x)):
        if int(x[j]) <= 255:
            pass
        else:
            print("Ip is Invalid!")