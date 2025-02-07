square=[1,2,3,4,5]
l=square
print(square)
print(l)
l2=square.copy()
print(l2)

square[0]=33
# print(square) # square will change
# print(l) # l will change
# print(l2) # value will no change beacuse l2 is a copy not source

print(square[1])
print(len(square))
print(square.count(2)) # count means count the values how many time 2 occures in the list [1,2,3,4,5] -> 1 times only
print(square[-2]) # minus - index will go reverse

print(square[0:2]) # Slicing <- 0 start index -> <- 2 value