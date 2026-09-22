import os
import sys
import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")

sys.path.insert(0, SRC_PATH)

from student import Student


@pytest.fixture
def make_student():
    """
    Function scope is useful when each test needs fresh, independent data.
    This fixture runs separately for every test that uses it.
    """
    Student.existing_roll_numbers.clear()

    def _make_student(name="Ali", roll_no=1000, scores=None):
        student = Student(name, roll_no)

        if scores:
            for score in scores:
                student.add_score(score)

        return student

    yield _make_student

    Student.existing_roll_numbers.clear()


@pytest.fixture(scope="module")
def sample_scores():
    """
    Module scope is appropriate for setup that is expensive and can
    safely be shared by all tests in the same module.
    """
    return [70, 80, 90]