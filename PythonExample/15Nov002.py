# How to read file
# File IO in python

file=open('pramod.txt', 'r')
print(file.read())
file.close()

# How to Write a file
# Append

# file2=open('pramod.txt','a')
# file2.write("Yes Yes")  # Append will add new data
# file2.close()

file=open('pramod.txt', 'r')
print(file.read())
file.close()

# Write

file2=open('pramod.txt','w')
file2.write("Yes Yes")  # Write will override
file2.close()

# If file is saved in different folder then copy path and paste in open ' '
# file3=open('PythonExample/pramod.txt','r')
# print(file3.read())
# file3.close()