# Write a Python program to prove that two string variables of the same value point to the same memory location.

var1 = "John"
var2 = "John"

print("address of var1 is = "+hex(id(var1)))
print("address of var2 is = "+hex(id(var2)))