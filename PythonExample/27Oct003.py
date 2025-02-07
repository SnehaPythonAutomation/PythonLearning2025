tuple3 = tuple(["pramod", "sneha", "python"])
# Merging of Tuples

hero1 = ("Batman", "Bruce Wyane")
hero2 = ("Wonder Women", "Diana Prince")
awsome_team = hero1 + hero2  # we can merge by using ' + ' concatination
print(awsome_team)
print(awsome_team[0])
print(awsome_team[1])

# Covert to list
my_tuple = (1, 2, 6, 4, 5, 7)
print(list(my_tuple))  # you can convert to list

# eg.,

x = 10
a, b = 30, 40  # This is Multiple values assign
q, w, e = (20, 85, 14)  # Tuple assign to multple variables

# Nested Tuples
hero1 = ("Batman", "Bruce Wyane")
hero2 = ("Wonder Women", "Diana Prince")
awsome_team = (hero1, hero2)  # two tuples combined
print(awsome_team)
print(awsome_team[0])
print(awsome_team[0][0])
print(awsome_team[0][1])
print(awsome_team[1])
print(awsome_team[1][0])
print(awsome_team[1][1])

#Serah-> In tuple
cities=("Paris","London","Korean","China" )
print("Paris" in cities)
print("Turkish" in cities)

