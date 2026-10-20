import pytest


@pytest.mark.parametrize(
    "score, should_raise",
    [
        (-10, True),
        (-1, True),
        (0, False),
        (50, False),
        (99, False),
        (100, False),
    ],
    ids=[
        "negative-10",
        "negative-1",
        "zero",
        "normal-score",
        "high-score",
        "hundred",
    ],
)
def test_add_score_cases(make_student, score, should_raise):
    student = make_student("Ali", 300)

    if should_raise:
        with pytest.raises(ValueError):
            student.add_score(score)
    else:
        student.add_score(score)
        assert score in student.scores