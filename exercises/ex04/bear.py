"""File to define Bear class."""


class Bear:

    def __init__(self, age: int = 0, hunger_score: int = 0):
        self.age = age
        self.hunger_score = hunger_score
        return None

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        self.hunger_score += num_fish
