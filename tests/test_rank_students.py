from gradebook import Roster, rank_students


def test_rank_students_empty_roster_returns_empty_list():
    roster = Roster()

    assert rank_students(roster) == []
    



def test_rank_students_single_student_returns_that_student(make_student):
    roster = Roster()
    student = make_student("Ali", 301, [80, 90])
    roster.add_student(student)

    assert rank_students(roster) == [student]



def test_rank_students_sorts_by_average_descending(make_student):
    roster = Roster()

    ali = make_student("Ali", 302, [60, 70])
    sara = make_student("Sara", 303, [90, 100])
    ahmed = make_student("Ahmed", 304, [75, 85])

    roster.add_student(ali)
    roster.add_student(sara)
    roster.add_student(ahmed)

    assert rank_students(roster) == [sara, ahmed, ali]
