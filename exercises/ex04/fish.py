"""File to define Fish class."""


class Fish:
    """Life changes of the fish in the river."""

    age: int

    def __init__(self, age: int = 0):
        """Newborn fish with an early start."""
        self.age = 0
        return None

    def one_day(self):
        """New fish age after a day at the river."""
        self.age += 1
        return None
