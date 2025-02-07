# Maps and Filters

sq=lambda x : x * x
result=sq(4)
print(result)

# Map Functions(Where will go from one item and apply a function)

numbers=[1,2,3,4,5]
# square of numbers [1,4,6,16,25]
sq_numbers=[]
for i in numbers:
    sq_numbers.append(sq(i))
    print(sq_numbers)

# Map Function (you can do with one line statement)

# map function will take twi argumet , function we want to run on which list
sq_numbers2=list(map(lambda x: x*x,numbers))