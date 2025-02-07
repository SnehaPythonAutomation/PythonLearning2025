# Task #3
#
#  Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
#
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
# Use an if-else statement to classify the triangle.
#
# 3 Input
#
# side 1, side 2 and side 3
#
# output - Eq, Iso, Scalene -
#
# Eq. = side 1 == side 2 = side 3



Length1= int(input("Enter the Length 1\n"))
Length2= int(input("Enter the Length 2\n"))
Length3= int(input("Enter the Length 3\n"))

if Length1 == Length2 == Length3 :
    print("Triangle is equilateral")

elif Length1 == Length2 or Length2 == Length3 or Length1 == Length3:
    print("Triangle is isosceles ")

else:
    print("Triangle is scalene")
