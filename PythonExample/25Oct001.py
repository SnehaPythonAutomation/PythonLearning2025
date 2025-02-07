# List -> collection of items(duplicates allowed)

my_list=[1,2,3]
my_list2=[1,True,"pramod",12.11]

print("Initial list:", my_list)

#Indexing
print("print the element at index 0:", my_list2[0])

#changing an element
my_list[1]=20
print("print list after changing an element at index 1:", my_list)

# append() -> means adding
my_list.append(4)
print("List after appending:", my_list)

#Extend -> we can extend with another list
my_list.extend([5,6])
print("Print List after extending:", my_list)

# insert -> we can insert values rest will be shifted
my_list.insert(1,'a')
print("Print List after insearting 'a' at index 1:", my_list)

#remove
my_list.remove('a')
print("Print List after removing 'a'", my_list)

#copy
my_copy_list=my_list.copy()
print("Copied list",my_copy_list)

#clear  -> It will be empty list
my_list.clear()
print("Initial List:", my_list)

#index
#print("print the element at index 3:", my_list[3])  # my_list we have clear()
print("print the element at index 3:", my_copy_list[3])

#sort() -> assending order will do sorting
my_copy_list.sort()
print(my_copy_list)

#reverse
my_copy_list.reverse()
print(my_copy_list)

# what is length of this
print(len(my_copy_list))

print(my_copy_list.remove(4)) # It gets remover 4 from list but it doesn't return anything i.e its none as per function.
print(my_copy_list) # 4 removed