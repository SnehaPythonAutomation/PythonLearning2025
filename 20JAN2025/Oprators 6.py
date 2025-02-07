# Identity - is, is not
# is 	Returns true if both variables are the same object	x is y
# is not	Returns true if both variables are not the same object	x is not y


x= [1,2,3]  # Identity oprators should only use with list, set, tuples, Dic, Table
y= [1,2,3]

print(x is y)
print(x is not y)

a=10
b=10
print(a is b)  # Identity oprators should not use with primitives means which are not list, set, tuples, Dic, Table