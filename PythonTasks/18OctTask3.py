# Example using break to exit a loop when i == 51 while printing the values from 1 to 100

count = 1
#while count <= 100:
#  print(count)
#if count >= 51:
#  break
#  count = count + 1

for count in range (1,100) :
    print(count)
    if count == 51 :
        break
        count = count + 1
