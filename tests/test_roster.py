import pytest

from gradebook import Roster


@pytest.mark.parametrize("score_count,should_raise", [
    (0, True),
    (3, False),
    (8, True),
])
def test_score_count_classes(make_student, score_count, should_raise):
    student = make_student(
        name="Ali Khan",
        roll_no=200 + score_count,
        scores=[50] * score_count
    )

    roster = Roster()

    if should_raise:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        roster.add_student(student)
        assert student in roster.students