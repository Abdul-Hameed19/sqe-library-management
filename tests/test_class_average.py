from gradebook import Roster


def test_class_average_multiple_students(make_student):
    roster = Roster()

    student1 = make_student("Ali", 201, [80, 80])
    student2 = make_student("Ahmed", 202, [90, 90])

    roster.add_student(student1)
    roster.add_student(student2)

    assert roster.class_average() == 85.0


def test_class_average_single_student(make_student):
    roster = Roster()

    student = make_student("Ali", 203, [70, 80])

    roster.add_student(student)

    assert roster.class_average() == 75.0


def test_class_average_empty_roster():
    roster = Roster()

    assert roster.class_average() == 0.0