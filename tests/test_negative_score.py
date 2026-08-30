import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import Student

student = Student("Ali")

try:
    student.add_score(-10)
    print("FAIL: Negative score was accepted")
except ValueError:
    print("PASS: Negative score was rejected")