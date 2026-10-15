# Worksheet 1.2: Task 1 Solution
import sys
grade_text = input("enter your grade")
if not grade_text.isdigit():
    
    print("Invalid input. Please enter a valid integer.")
    sys.exit("grade must be an integer between 0 and 100")
grade=int(grade_text)
if grade <0 or grade>100:
     print("Invalid input. Please enter a valid integer.")
     sys.exit("grade must be an integer between 0 and 100")
if grade <40:
    print(grade,"is a Fail")
elif grade >=40 and grade <70:
    print(grade,"is a Pass")
else:
    print(grade,"is a Distinction")