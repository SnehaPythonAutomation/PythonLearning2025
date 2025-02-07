phone_book= {"Batman" : 985412578, "supeman" : 428745124, "Wonder" : 5412547896}

# Dict ? It is very close to JSON

print(phone_book)
print(len(phone_book))

print(phone_book["Batman"])
print(phone_book["Wonder"])  #By using Key we have to access the values- for accessing element only key will be used.

phone_book2=dict(Batman= 123654,Superman=12458,Wonder=46875)
print(phone_book2)
print(phone_book2["Batman"]) #or
print(phone_book2['Batman']) # or
print(phone_book2.get('Batman'))

new_dict=dict(name="pramod",age=34, isMale=True,address="India")   # 54=60 not accepting
new_dict2={"name":"pramod", "age":34, 54:60,"isMale":True,"address":"India"}
print(new_dict)
print(new_dict2)

my_dict3={'a':1 , 'b':3, 'c' : 99, 'a' : 99 }  # IN this kay 'a' will take latest value only and values can be duplicate not keys ...
print(my_dict3)

# How to get all Keys and all values using key() function

keys=my_dict3.keys()
values=my_dict3.values()
print(keys)
print(values)

#Get all keys into list
list_keys=list(keys)  # we can convert keys into list
print(list_keys)
list_values=list(values) # we can convert values into list
print(list_values)
print(list_keys[0])  # and here now we can access them by index after converting
print(list_keys[1])
print(list_keys[2])

set_my_dict3=set(my_dict3.items())   #If you want all items -> a set like object providing -> so coverting them to a set
print(set_my_dict3 )
