import sys
sys.path.append("..")

from student import Student

student = Student("Ali", 101)

student.add_score(80)
student.add_score(81)
student.add_score(83)

print(student.average())