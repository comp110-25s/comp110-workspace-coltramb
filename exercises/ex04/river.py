"""File to define River class!"""

__author__ = "730575668"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """I am creating a River Simulation."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Will assess bear and fish ages and adjust accordingly."""
        living_fish: list[Fish] = []
        living_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                living_fish.append(fish)
        self.fish = living_fish
        for bear in self.bears:
            if bear.age <= 5:
                living_bears.append(bear)
        self.bears = living_bears
        return None

    def bears_eating(self):
        """Result after bears eat on the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

        return None

    def check_hunger(self):
        """Hunger of the animals check-in."""
        living_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                living_bears.append(bear)
        self.bears = living_bears
        return None

    def repopulate_fish(self):
        """The river being repopulated with fish."""
        num_fish = len(self.fish)
        new_fish_living: list = []
        num_new_fish = (num_fish // 2) * 4
        while num_new_fish > 0:
            new_fish_living.append(Fish())
            num_new_fish -= 1
        self.fish += new_fish_living
        return None

    def repopulate_bears(self):
        """The river being repopulated with bears."""
        num_bears = len(self.bears)
        num_new_bears = num_bears // 2
        count: int = 0
        while count < num_new_bears:
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Will show the population numbers in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Shows what a week at the river is like."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
        return None

    def remove_fish(self, amount: int):
        """Takes away fish that are eaten from the count."""
        while amount > 0 and self.fish:
            self.fish.pop(0)
            amount -= 1
        return None
