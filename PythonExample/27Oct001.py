my_list=[1,2,4,6,8] # list
print(my_list)
my_list[0]=30 # we can assign values in list
print(my_list)

#List :
# List is mutable its content can be change.

#Tuple :
#
car=("Ford", "Audi", "BMW")
car2=("Ford",True,3.2,50, "Audi", "BMW") # Tuple can have multipledatatype
print(car)
#car[0]="Swift" # In Tuple content cannot be change Its means its is immutable in nature
print(car)

print(len(car))

# Tuple and list both can have duplicates entries

#List canbe converted to Tuple
list1=[1,8,7,9,10]
print(list1)
print(tuple(list1))