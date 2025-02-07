# If file not found , file doesn't have in system user trying to read then how to handle exception

try:
    file = open('pramod2.txt', 'r')
    print(file.read())
except FileNotFoundError as e:
    print("No such file in system", e)
except IOError as e:
    print("Error occured while reading file")
else:
    print("File reading completed successfully")