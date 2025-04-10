"""File to define Bear class."""


class Bear:
    """Bears near the river."""


def __init__(self, age: int, hunger_score: int):
    """As a newborn, age is zero."""
    self.age = 0
    self.hunger_score = 0
    return None


def one_day(self):
    """Changes in age and hunger one day after the river."""
    self.age += 1
    self.hunger_score -= 1
    return None


def eat(self, num_fish: int):
    """Status of river once the bears have eaten."""
    self.hunger_score += num_fish
    return None
