import pytest
from gradebook import Roster, percentile


def test_percentile_empty_roster_returns_zero(make_student):
    roster = Roster()
    student = make_student("Ali", 401, [80, 90])

    assert percentile(student, roster) == 0.0


def test_percentile_single_student_returns_100(make_student):
    roster = Roster()
    student = make_student("Ali", 402, [80, 90])
    roster.add_student(student)

    assert percentile(student, roster) == 100.0


def test_percentile_highest_average_returns_100(make_student):
    roster = Roster()

    ali = make_student("Ali", 403, [40, 50])
    sara = make_student("Sara", 404, [90, 100])
    ahmed = make_student("Ahmed", 405, [60, 70])

    roster.add_student(ali)
    roster.add_student(sara)
    roster.add_student(ahmed)

    assert percentile(sara, roster) == 100.0


def test_percentile_lowest_average_returns_zero(make_student):
    roster = Roster()

    ali = make_student("Ali", 406, [40, 50])
    sara = make_student("Sara", 407, [90, 100])
    ahmed = make_student("Ahmed", 408, [60, 70])

    roster.add_student(ali)
    roster.add_student(sara)
    roster.add_student(ahmed)

    assert percentile(ali, roster) == 0.0


def test_percentile_equal_averages_get_same_percentile(make_student):
    roster = Roster()

    ali = make_student("Ali", 409, [60, 80])
    ahmed = make_student("Ahmed", 410, [70, 70])
    sara = make_student("Sara", 411, [90, 100])

    roster.add_student(ali)
    roster.add_student(ahmed)
    roster.add_student(sara)

    assert percentile(ali, roster) == pytest.approx(0.0)
    assert percentile(ahmed, roster) == pytest.approx(0.0)