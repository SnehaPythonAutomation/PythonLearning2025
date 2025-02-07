num=20

def multiply_by_10(n) :   # define the function
    n *= 10
    num=n    # changing value inside the function
    print("Value of num inside function:", num)
    return  n

multiply_by_10(num)  # called the function   # excecution for num=200 is from line 1 to 9
print("Value of the num outside function:", num)