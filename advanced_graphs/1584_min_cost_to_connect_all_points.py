"""
1584. Min Cost to Connect All Points
------------------------------------
Difficulty: Medium

You are given a 2-D integer array points,
where points[i] = [xi, yi].
Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj]
is the manhattan distance between the two points,
i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together,
such that there exists exactly one path between each pair of points.

Examples:
Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
Output: 10

Constraints:
1 <= points.length <= 1000
-1000 <= xi, yi <= 1000
"""
import heapq


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


def min_cost_connect_points_kruskal(
    points: list[tuple[int, int]]
) -> int:
    """
    Time complexity: O(n^2 * log n)
    Space complexity: O(n^2)
    """
    dsu: DisjointSetUnion = DisjointSetUnion(len(points))
    edges: list[tuple[int, int, int]] = []
    for i, point in enumerate(points):
        x1, y1 = point
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            distance: int = abs(x1 - x2) + abs(y1 - y2)
            edges.append((distance, i, j))

    edges.sort()
    total_cost = sum(distance for distance, u, v in edges if dsu.union(u, v))
    return total_cost


def min_cost_connect_points_prim(points: list[tuple[int, int]]) -> int:
    """
    Time complexity: O(n^2 * log n)
    Space complexity: O(n^2)
    """
    size = len(points)
    adjacencies: dict[int, list[tuple[int, int]]] = {i: [] for i in range(size)}
    for i, point in enumerate(points):
        x1, y1 = point
        for j in range(i + 1, size):
            x2, y2 = points[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            adjacencies[i].append((distance, j))
            adjacencies[j].append((distance, i))

    total_cost = 0
    visited_nodes: set = set()
    min_heap: list[tuple[int, int]] = [(0, 0)]  # (cost, point index)
    while len(visited_nodes) < size:
        cost, node_index = heapq.heappop(min_heap)
        if node_index in visited_nodes:
            continue

        total_cost += cost
        visited_nodes.add(node_index)
        for neighbour_cost, neighbour_index in adjacencies[node_index]:
            if neighbour_index not in visited_nodes:
                heapq.heappush(
                    min_heap, (neighbour_cost, neighbour_index)
                )

    return total_cost


def min_cost_connect_points_prim_optimised(points: list[tuple[int, int]]) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    size = len(points)
    node: int = 0
    distances: float[int] = [float('inf')] * size
    are_visited: list[bool] = [False] * size
    num_edges = 0
    total_cost = 0
    while num_edges < size - 1:
        are_visited[node] = True
        next_node = -1
        for i, point in enumerate(points):
            if are_visited[i]:
                continue

            current_distance = (
                abs(point[0] - points[node][0])
                + abs(point[1] - points[node][1])
            )
            distances[i] = min(distances[i], current_distance)
            if next_node == -1 or distances[i] < distances[next_node]:
                next_node = i

        total_cost += distances[next_node]
        node = next_node
        num_edges += 1

    return total_cost


def test_min_cost_connect_points():
    solutions = [
        min_cost_connect_points_kruskal,
        min_cost_connect_points_prim,
        min_cost_connect_points_prim_optimised,
    ]

    test_cases = [
        ([(0, 0), (2, 2), (3, 3), (2, 4), (4, 2)], 10),
    ]

    for solution in solutions:
        for points, expected_min_cost in test_cases:
            # Act
            min_cost_connect_points = solution(points)

            # Assert
            assert expected_min_cost == min_cost_connect_points

        print(f'Tests passed for {solution.__name__}')



if __name__ == '__main__':
    test_min_cost_connect_points()