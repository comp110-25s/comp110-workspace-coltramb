class Node:
    def __str__(self) -> str:
    return f"{self.value} -> {self.next}"


courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)


def last(head: Node) -> int:
    if head.next is None:  # Base case
        return head.value
    else:
        return last(head.next)  # Recursive case
