class Node:
    def __init__(self, value, neighbours: list['Node'] | None = None):
        self.value = value
        self.neighbours = neighbours or []

    def equal_value(self, other: 'Node') -> bool:
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return f'Node({self.value}, neighbours={[n.value for n in self.neighbours]})'

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        return (
            self.equal_value(other)
            and all(
                n.equal_value(on) for n, on in zip(self.neighbours, other.neighbours)
            )
        )
