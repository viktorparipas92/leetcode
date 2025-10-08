class DisjointSetUnion:
    def __init__(self, n: int):
        self.parent: list[int] = list(range(n + 1))
        self.size: list[int] = [1] * (n + 1)

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u: int, v: int) -> bool:
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return False

        if self.size[parent_u] < self.size[parent_v]:
            parent_u, parent_v = parent_v, parent_u

        self.size[parent_u] += self.size[parent_v]
        self.parent[parent_v] = parent_u
        return True

    def is_connected(self, u: int, v: int):
        return self.find(u) == self.find(v)