
import re

# Constants
MAX_SCORE = 100
MAX_NAME_LENGTH = 50
MIN_SCORES = 1
MAX_SCORES = 6

GRADE_THRESHOLDS = {
    "F": 59,
    "D": 69,
    "C": 79,
    "B": 89,
}

NAME_PATTERN = re.compile(r"[A-Za-z -]+")


class GradeBookIOError(Exception):
    pass


def letter_grade(score):
    if score < 0 or score > MAX_SCORE:
        raise ValueError("Score must be between 0 and 100")

    if score <= GRADE_THRESHOLDS["F"]:
        return "F"
    elif score <= GRADE_THRESHOLDS["D"]:
        return "D"
    elif score <= GRADE_THRESHOLDS["C"]:
        return "C"
    elif score <= GRADE_THRESHOLDS["B"]:
        return "B"
    else:
        return "A"


def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty")

    if len(name) > MAX_NAME_LENGTH:
        raise ValueError("Name cannot exceed 50 characters")

    if not NAME_PATTERN.fullmatch(name):
        raise ValueError(
            "Name can contain only letters, spaces, and hyphens"
        )

    return True


class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        score_count = len(student.scores)

        if score_count < MIN_SCORES or score_count > MAX_SCORES:
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
                    scores = ",".join(
                        str(score) for score in student.scores
                    )
                    line = f"{student.name},{student.roll_no},{scores}\n"
                    file.write(line)
        except OSError as e:
            raise GradeBookIOError(
                "Could not save roster to file"
            ) from e


def rank_students(roster):
    return sorted(
        roster.students,
        key=lambda student: (-student.average(), student.name.lower())
    )


def percentile(student, roster):
    total_students = len(roster.students)

    if total_students == 0:
        raise ValueError("Roster cannot be empty")

    rank_index = sum(
        1 for s in roster.students
        if s.average() < student.average()
    )

    return (rank_index / total_students) * 100
