# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59


grade = int(input("Enter the Numerical score to display Grade\n"))

# print("A" if grade>=90 and grade<=100 elif "B" if grade>=80 and grade<=89 elif "C" if grade>=70 and grade<=79
# elif "D" if grade>=60 and grade<=69 elif "F" if grade>=0 and grade<=59)

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
else:
    print("F")
