# Week 1.3, Session 1: Task 5a

course = "computer science"
course_list = list(course)
course_list.sort()
new_list= []

for ch in course:
    print(ch)
    new_list.append(ch)

sorted(new_list)
print(new_list)

# create a list data structure of the characters from the course string
# sort the list into alphabetical order