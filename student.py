class Student:
    existing_roll_numbers = set()

    def __init__(self, name, roll_no):
        if roll_no in Student.existing_roll_numbers:
            raise ValueError("Roll number already exists")

        self.name = name
        self.roll_no = roll_no
        self.scores = []

        Student.existing_roll_numbers.add(roll_no)

    def add_score(self, score_value):
        if score_value < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score_value)

    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)