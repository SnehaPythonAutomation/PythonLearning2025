# Task #1

# Explain the difference between the = operator and the == operator in Python.
#      ->>>> The = operator is used for assignment, such as when assigning a value to a variable.
#            The == operator is the relational operator for checking equality of two values.
#            If the values are the same, it will return True, and will return False otherwise.


# What does the ** operator do in Python, and how is it used?
# ->> The square of 3 is 9 - mathematically.
x = 10
b = 3

result = (x ** b)
print(result)

print("--------------------------------------------")

# What does the ^ operator do in Python, and in what context is it commonly used?
x = 10
b = 3

result = (x ^ b)
print(result)

print("--------------------------------------------")
#
# Task #2
#
# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)
#
pi = 3.14
r = 9 ** 2
area = pi * r
print("Area of circle is", area)


print("--------------------------------------------")
#
#
# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

Num1 = int(input("Enter the first number\t"))
Num2 = int(input("Enter the Second number\t"))

if Num1 > Num2:
    print(Num1, "is greater than", Num2)
elif Num1 < Num2:
    print(Num1, "is less than", Num2)
else:
    print(Num1, "is equal to", Num2)

    print("-----------------------------------------------------------------------")
# Use the ternary operator to find the maximum of three numbers entered by the user.
Num3=int(input("Enter the Third number\t"))
max_val = Num1 if Num1 > Num2 and Num2 > Num3 else Num2 if Num2 > Num3 and Num2 > Num1 else Num3
print("Max value is", max_val)

print("-----------------------------------------------------------------------")
# Develop a Python script that calculates the square and cube of a given number.

square= Num1 ** 2
print("Entered number square is", square)
cube= Num1 ** 3
print("Entered number cube is", cube)
