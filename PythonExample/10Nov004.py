# Exceptions
# An exception is an event that occurs during the execution of a program that disturpts the normal flow of instructions.

# we need to handle errors
a = 10
b = 0

try:
    c = a / b
except Exception as error:
    print(error)


#eg-,2)

a=int(input("Enter the A number"))
b=int(input("Enter the B number"))
try:
   c=a/b
   print(c)
except Exception as error:
    print("You are dividing the value of A with zero, don't do it", error)
