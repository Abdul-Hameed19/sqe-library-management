import pytest


def test_negative_score_rejected(make_student):
    student = make_student("Ali", 102)

    with pytest.raises(ValueError):
        student.add_score(-10)