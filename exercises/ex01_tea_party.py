"""I am planning a tea party budget."""

__author__: str = "730575668"


def main_planner(guests: int) -> None:
    """Entrypoint of the program."""
    print("A Cozy Tea Party for " + str((guests)) + " People! ")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """The number of tea bags needed for the party."""
    return people * 2


def treats(people: int) -> int:
    """The number of treats needed for guest teas"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """The total cost of tea bags and treats."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
