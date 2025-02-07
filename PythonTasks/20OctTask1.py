# Palindrome Checker:
# Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
# Example - pramod
# madam - reverse(madam) -> same
# Naman -> reverse -> same
# Malayalam
#
# def reverse_string(input_string):
#     reverse_str = ""
#     for char in input_string:
#         reverse_str = char + reverse_str
#     return reverse_str
#
#
# original_str = "abcd"
# rev_str = reverse_string(original_str)
# print(rev_str)
#
# if original_str == rev_str:
#     print("This is Palindrome")
# else:
#     print("This is not Palindrome")
#
# #another way..
#
# input_string=input("Enter the string\n")
# reverse_str=(input_string[: : -1])
# print(reverse_str)
# if reverse_str == input_string :
#     print("This is Palindrome")
# else :
#     print("It is not")

# another way..

original_string = input("Enter the string")


def reverse_string(original_string):
    return ''.join(reversed(input(original_string)))


rev_str = reverse_string(original_string)
print(rev_str)

