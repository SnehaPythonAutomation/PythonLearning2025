#Exceptions in Python

try:
    x = int(input("Enter a number:"))
    result = 10 / x
    print(result)
except ZeroDivisionError as error: # you can give parent also like except Exception as error: or individually "ZeroDivisionError"
    #except Exception as error: parent exception
    print("Error", error)
except ValueError as error:
    print("Error", error)
finally:
    print("I will be excecuted any how")

# Division by zero- ZeroDivisionError: division by zero
# String or nothing- ValueError: invalid literal for int() with base 10: 'pramod'
# Negative- Fine
# None- ValueError:invalid literal for int() with base10: 'None'
# Float: ValueError: invalid literal for int() with base10: '43.23'
# complex : ValueError: invalid literal for int() with base10: '1+8j'
# ABC123: ValueError: invalid literal for int() with base10: 'ABC123'
# True: ValueError: invalid literal for int() with base10: 'True'
# @!!: ValueError: invalid literal for int() with base10: '@!!'
# (), [] - ValueError: invalid literal for int() with base10: '[1,2,3,4,5]'

# so to handle this Exception(error) we use Try except
