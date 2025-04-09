"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for i in range(0, num_fish):
            self.fish.append(Fish())
        for i in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        living_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                living_fish.append(fish)
        self.fish = living_fish

        living_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                living_bears.append(bear)
        self.bears = living_bears
        return None

    def remove_fish(self, amount: int):
        for i in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)

    def bears_eating(self):
        if len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        living_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                living_bears.append(bear)
        self.bears = living_bears
        return None

    def repopulate_fish(self):
        num_new_fish = (len(self.fish) // 2) * 4
        for i in range(num_new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        num_new_bears = len(self.bears) // 2
        for i in range(num_new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        for i in range(7):
            self.one_river_day()
