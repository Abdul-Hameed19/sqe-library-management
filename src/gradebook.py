
import re


class GradeBookIOError(Exception):
    pass


def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score <= 59:
        return "F"
    elif score <= 69:
        return "D"
    elif score <= 79:
        return "C"
    elif score <= 89:
        return "B"
    else:
        return "A"


def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty")

    if len(name) > 50:
        raise ValueError("Name cannot exceed 50 characters")

    if not re.fullmatch(r"[A-Za-z -]+", name):
        raise ValueError(
            "Name can contain only letters, spaces, and hyphens"
        )

    return True


class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        score_count = len(student.scores)

        if score_count < 1 or score_count > 6:
            raise ValueError("Student must have between 1 and 6 scores")

        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0

        total = sum(student.average() for student in self.students)
        return total / len(self.students)

    def save_to_file(self, path):
        try:
            with open(path, "w") as file:
                for student in self.students:
                    scores = ",".join(str(score) for score in student.scores)
                    line = f"{student.name},{student.roll_no},{scores}\n"
                    file.write(line)
        except OSError as e:
            raise GradeBookIOError(
                "Could not save roster to file"
            ) from e


def rank_students(roster):
    return []
