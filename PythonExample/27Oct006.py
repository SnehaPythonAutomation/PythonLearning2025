
set1={1,2,3}
set2={4,5,6}
my_set=set1.union(set2)   #Union means all the elements
print(my_set)

set1={1,2,3,4,5}
set2={4,5,6,3,8}
my_set2=set1.intersection(set2)  # Intersection means common values between two set
print(my_set2)

set1={1,2,3,4,5}
set2={4,5,6,3,8}
my_set2=set1.difference(set2)  # Difference means difference values between set1 will print
my_set3=set2.difference(set1)  # Difference means difference values between set2 will print
print(my_set2)
print(my_set3)

#Function Subset()
set1={1,2,3,4,5}
set2={1,2,3}
my_set4= set2.issubset(set1)
print(my_set4)
