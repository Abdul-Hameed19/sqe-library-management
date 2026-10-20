import pytest


def test_duplicate_roll_number_rejected(make_student):
    make_student("Ali", 101)

    with pytest.raises(ValueError):
        make_student("Ahmed", 101)