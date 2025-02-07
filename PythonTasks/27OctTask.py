# # 1. Write a Python program to find the largest number in a list.

number=[45,55,87,46,12,85,41,97]
print(number)
largestnumber= max(number)
print("Largest number in List is:",largestnumber)

# # 2. Write a Python program to find the smallest number in a list

number2=[45,55,87,46,12,85,41,97]
print(number2)
smallestnumber= min(number2)
print("Smallest number in List is:",smallestnumber)

# # 3. Write a Python program to sum all numbers in a list.

number3=[45,55,87,46,12,85,41,97]
print(number3)
sumofnumbers= sum(number3)
print("sum of numbers in List is:",sumofnumbers)

# 4. Write a Python program to multiply all numbers in a list.

number4=[45,55,87,46,12,85,41,97]
def multiply_all_numbers(number4) :
    count=1
    for i in number4 :
        count *= i
    return  count
count=multiply_all_numbers(number4)
print("Multiplication of all numbers is:", count)


# 5. Write a Python program to count the number of strings in a list where the string length is 2 or more and
# the first and last character are the same


list = ["snehs", "yada", "neru", "pythop"]

def count_numbers_of_string_first_last_same(list):
    count = 0
    for s in list:
        if len(s) >= 2 and s[0] == s[-1]:
         count += 1
    return count
result = count_numbers_of_string_first_last_same(list)
print("Number of strings with the same first and last character: ", result)



