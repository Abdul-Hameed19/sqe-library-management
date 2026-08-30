import sys
sys.path.append("..")

from student import Student

student1 = Student("Ali", 101)
student2 = Student("Ahmed", 101)

print(student1.roll_no)
print(student2.roll_no)