# String
# Bunch of characters
name="sneha"


#String Functions
#Python String Immutable in nature - They can't be chaanged, once created
# name[0]="h" # TypeError: 'str' object does not support item assignment
# whenever we use functions() it will create new string
#capetalize

result=name.capitalize()
# Return a capitalized version of the string.
# More specifically, make the first character have upper case and the rest lower case.
print(result)
print(name)

# Upper case
result2=name.upper()
print(result2)


# lower case
result3=name.lower()
print(result3)

# Swapcase()
#Convert uppercase characters to lowercase and lowercase characters to uppercase.
name="SnEhA"
result4=name.swapcase()
print(result4)

# Title
# Return a version of the string where each word is titlecased.
# More specifically, words start with uppercased characters and all remaining cased characters have lower case.
name=" hello world"
print(name.title())

# Replace
text="hello world"
result_rep= print(text.replace("world","python"))

# find()
# Return the lowest index of a substring in the string
# Returns -1 if the substring is not found

text="hello world"

result_find=text.find("world")
print(result_find)

# Count()
count= text.count("l")
print(count)

# None Type
val=None
# None is not the same as False
# None is not an empty string
# None is not 0
print(val)

# Delete
name="yadav"
print(name)
# del name
# print(name)

# String Formatting
string="I Like %s" % "Python"
print(string)

name=input("Enter your name\n")
print(name)
print("Your name is %s" % name)


# String. format
