# Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
# n = 12345
# sum = 15
# n = 123
# sum = 6


#
num = int(input("Enter the number\n"))
sum = 0
while num != 0:
    digit = num % 10
    sum = sum + digit
    num = int(num / 10)
print(sum)
