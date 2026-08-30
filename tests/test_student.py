import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import Student

student = Student("Ali", 101)

print(student.average())