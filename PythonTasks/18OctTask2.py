# Factorial Program

# n= 5
# 5!= 5 * 4 * 3 * 2 * 1 = 120
# 3!= 3 * 2 * 1 =  6
# 4!= 4 * 3 * 2 * 1 = 24

number = int(input("Enter the number\n"))
if number < 0:
    print("Factorial Not Posiible")
else:
    fact = 1                                  # Logic
    for i in range(1, number + 1):            # for loop range starts from 0 , len-1
        fact = fact * i                       #  range will go 1 to 5 > number +1 > will go 1 to 6
    print("Factorial of ->", fact)            # number=5
                                              # i=1 , fact= 1,  fact= 1 * 1   fact=1
                                              # i=2 , fact= 1,  fact= 1 * 2 fact = 2
                                              # i=3, fact=2 , fact = 2 * 3 fact = 6
                                              # i=4, fact=6 , fact= 6 * 4 fact = 24
                                              # i=5, fact=24 , fact= 24 * 5 fact = 120