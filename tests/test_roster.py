import pytest

from gradebook import Roster
from student import Student


@pytest.mark.parametrize("score_count,should_raise", [
    (0, True),
    (3, False),
    (8, True),
])
def test_score_count_classes(score_count, should_raise):
    student = Student("Ali Khan", 200 + score_count)

    for score in range(score_count):
        student.add_score(50)

    roster = Roster()

    if should_raise:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        roster.add_student(student)
        assert student in roster.students


@pytest.mark.parametrize("score_count,should_raise", [
    (0, True),
    (1, False),
    (2, False),
    (5, False),
    (6, False),
    (7, True),
])
def test_score_count_boundaries(score_count, should_raise):
    student = Student("Ali Khan", 300 + score_count)

    for score in range(score_count):
        student.add_score(50)

    roster = Roster()

    if should_raise:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        roster.add_student(student)
        assert student in roster.students