my_dict={'a' : 1, 'b' : 2}
val=my_dict.pop('a')
print(val)   # It will remove value 1

print(dir(my_dict))  # you will get all functions that will be used in Dictionary


# How to Iterate over the dictionary?  Iteration means we want to print all values
knights={'allahad' : 'the pure', 'robin' : 'the brave'}
print(len(knights))

for k,v in knights.items():
    print(k)
    print(v)

