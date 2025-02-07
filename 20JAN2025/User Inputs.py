# How to take Inputs from user?

name=input("Enter your name")
print(name)

# Task 1 - Take first name and last name of user and print with sep="_" and end with "/t"
name1="Sneha"
name2="yadav"
print((name1),(name2),sep="_")

print('--------------------------')

# Task 2 - Take user input as name and say with massage as You are Wellcome "<Sneha>" to the python class
output1=input("Enter your full name")
output2 = "You are Wellcome to the python class"
print((output1),(output2))

print('--------------------------')

#Adding two numbers with user inputs

num1= input("Enter the num1\n")
num2=input("Enter thee num2\n")

num1= int(num1)
num2= int(num2)

result=num1 + num2
print("The Sum is",result)