"""Creating linked list utils."""

__author__ = "730575668"

class Node:
    """Node in a singly-linked list recursive structure."""
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

        def value_at(head: Node | None, index: int) -> int:
            if head is None:
                raise IndexError("Index is out of bounds on the list.")
            if index == 0
                return head.value
            return value_at(head.next, index - 1)

        def max(head: Node | None) -> int:
            if head is None:
                raise ValueError("Cannot call max with None.")
            if head.next is None:
                return head.value
            max_in_rest = max(head.next)
            if head.value > max_in_rest:
                return head.value
            else:
                return max_in_rest
        def linkify(items: list[int]) -> Node | None:
            if len(items) == 0:
                return None
            else:
                return Node(items[0], linkify(items[1:]))
            
        def scale(head: Node | None, factor: int) -> Node | None:
            if head is None:
                return None
            else:
                return Node(head.value * factor, scale(head.next, factor))