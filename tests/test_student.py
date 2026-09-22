def test_student_average(make_student):
    student = make_student("Ali", 103, [80, 90, 100])

    assert student.average() == 90.0