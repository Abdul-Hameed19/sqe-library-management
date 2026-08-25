class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score_value):
        if score_value < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score_value)

    def average(self):
        return sum(self.scores) / len(self.scores)
