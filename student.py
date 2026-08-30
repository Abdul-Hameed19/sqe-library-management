class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []

    def add_score(self, score_value):
        self.scores.append(score_value)

    def average(self):
        if not self.scores:
            return 0.0
        return round(sum(self.scores) / len(self.scores), 1)

    def is_same_name(self, other_name):
        return self.name == other_name