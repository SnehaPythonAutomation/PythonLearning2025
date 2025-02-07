#
# def Hello():
#     print("Code that you want to execute")
# Hello()
#
#
# # function with parameter
# def functionWithPara(a):
#     return a**2
#
#
# output=functionWithPara(2)
# print(output)
#
# # eg..,
# def functionWithPara2(a,b):
#     return a*b
# output2=functionWithPara2(2,3)
# print(output2)

# lambda expression

functionwithpara=lambda a,b : a*b
print(functionwithpara(2,3))

additionwithpara=lambda a,b : a+b
print(additionwithpara(2,3))

sayHello= lambda name : print("your name is", name)
sayHello("Sneha")