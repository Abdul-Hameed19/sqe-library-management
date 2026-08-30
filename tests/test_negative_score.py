import sys
sys.path.append("..")

from student import Student

student = Student("Ali")
student.add_score(-10)

print(student.scores)