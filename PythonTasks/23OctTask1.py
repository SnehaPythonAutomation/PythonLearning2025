# Count vowels and consonants in a String
# aeiou
# input = pramod
# vol = 2


# count=0
# for i in user_input:
#
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
#         count= count + 1
# #         print("Number of vowles are" , count)
# user_input=input("Enter the string")
# def count_vowles(user_input) :
#     count=0
#     vowles=set("aeiou")
#     for alphabet in user_input :
#         if alphabet in vowles :
#             count=count+1
#             print("No of vowles are:", count)
# count_vowles(user_input)

vowels = 'a', 'e', 'i', 'o', 'u'
user_input = input("Enter the string\n")
count = 0
for alphabet in user_input:
    if alphabet in vowels:
        count = 1 + count
print("No of vowels in string are:" , count)