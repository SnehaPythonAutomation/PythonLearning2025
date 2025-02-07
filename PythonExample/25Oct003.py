square=[1,2,4,5,6] # List- allow duplicates # List is mutable in nature we can change the value
print(type(square))
square_tuple=(1,2,4,5,6)
print(type(square_tuple))

# how can we check list is empty

list=[]
if not list:
    print("Empty")
else:
    print("Not Empty")

#pop()
square=[1,2,4,5,6]

print(square.pop(2)) # pop function will remove the index
print(square)

print(square.remove(2)) # remove
print(square)