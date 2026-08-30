import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import Student

student1 = Student("Ali", 101)

try:
    student2 = Student("Ahmed", 101)
    raise AssertionError("Duplicate roll number was accepted")
except ValueError:
    print("PASS: Duplicate roll number is rejected")