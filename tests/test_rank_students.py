from gradebook import Roster, rank_students


def test_rank_students_empty_roster_returns_empty_list():
    roster = Roster()

    assert rank_students(roster) == []
    



def test_rank_students_single_student_returns_that_student(make_student):
    roster = Roster()
    student = make_student("Ali", 301, [80, 90])
    roster.add_student(student)

    assert rank_students(roster) == [student]

    