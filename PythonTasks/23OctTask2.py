# Create a Function with a Parameter which can do x^y
# eg., 2 ^ 6 = 2*2*2*2*2*2 = 64

# def powerOf(x,y) :
#     return x ** y
# print(powerOf(2,6))
#
# powerOf=lambda x,y : x ** y
# print(powerOf(2,6))
#
# # Create a Lambda expression to triple power 2**3 a number
#
# triplepower=lambda x , y : x ** 3
# print(triplepower(4,3))


# Right Triangle Star Pattern
# *
# **
# ***
# ****
# *****



# n = 5
# for i in range(0, n):
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print()

number= 5
count=1
for i in number(0,number) :
    count=i*count
    print("*",end=" ")