import sys
sys.path.append("..")

from student import Student

student = Student("Ali", 101)

print(student.is_same_name("ali"))