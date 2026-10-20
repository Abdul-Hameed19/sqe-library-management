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


def test_rank_students_sorts_equal_averages_alphabetically(make_student):
    roster = Roster()

    sara = make_student("Sara", 305, [80, 90])
    ali = make_student("Ali", 306, [85, 85])
    ahmed = make_student("Ahmed", 307, [90, 80])

    roster.add_student(sara)
    roster.add_student(ali)
    roster.add_student(ahmed)

    assert rank_students(roster) == [ahmed, ali, sara]



def test_rank_students_tie_breaking_ignores_name_case(make_student):
    roster = Roster()

    ali = make_student("ali", 308, [80, 90])
    Ahmed = make_student("Ahmed", 309, [85, 85])
    Bilal = make_student("BILAL", 310, [90, 80])

    roster.add_student(ali)
    roster.add_student(Ahmed)
    roster.add_student(Bilal)

    assert rank_students(roster) == [Ahmed, ali, Bilal]


def test_rank_students_places_zero_average_after_positive_average(make_student):
    roster = Roster()

    zero_student = make_student("Ali", 311, [0, 0])
    high_student = make_student("Sara", 312, [80, 90])

    roster.add_student(zero_student)
    roster.add_student(high_student)

    assert rank_students(roster) == [high_student, zero_student]