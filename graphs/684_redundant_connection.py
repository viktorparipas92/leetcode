"""
684. Redundant Connection
-------------------------
Difficulty: Medium

You are given a connected undirected graph with n nodes labeled from 1 to n.
Initially, it contained no cycles and consisted of n-1 edges.

We have now added one additional edge to the graph.
The edge has two different vertices chosen from 1 to n,
and was not an edge that previously existed in the graph.

The graph is represented as an array edges of length n where
edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

Return an edge that can be removed
so that the graph is still a connected non-cyclical graph.
If there are multiple answers, return the edge that appears last in the input edges.

Example 1:
Input: edges = [[1,2],[1,3],[3,4],[2,4]]
Output: [2,4]

Example 2:
Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
Output: [3,4]

Constraints:
n == edges.length
3 <= n <= 100
1 <= edges[i][0] < edges[i][1] <= edges.length
There are no repeated edges and no self-loops in the input.
"""


def find_redundant_connection_cycle_detection_dfs(
    edges: list[list[int]]
) -> list[int]:
    """
    Time complexity: O(E * (V + E))
    Space complexity: O(V + E)
    """
    def depth_first_search(node, parent):
        if visited_nodes[node]:
            return True

        visited_nodes[node] = True
        for neighbour in adjacency_list[node]:
            if neighbour == parent:
                continue

            if depth_first_search(neighbour, node):
                return True

        return False

    num_edges: int = len(edges)
    adjacency_list: list[list[int]] = [[] for _ in range(num_edges + 1)]

    for node_1, node_2 in edges:
        adjacency_list[node_1].append(node_2)
        adjacency_list[node_2].append(node_1)
        visited_nodes: list[bool] = [False] * (num_edges + 1)

        if depth_first_search(node=node_1, parent=-1):
            return [node_1, node_2]

    return []


def test_find_redundant_connection():
    solutions = [
        find_redundant_connection_cycle_detection_dfs,
    ]

    test_cases = [
        ([[1, 2], [1, 3], [3, 4], [2, 4]], [2, 4]),
        ([[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], [3, 4]),
    ]

    for solution in solutions:
        for edges, expected_redundant_edge in test_cases:
            # Act
            redundant_edge = solution(edges)

            # Assert
            assert redundant_edge == expected_redundant_edge

        print(f'{solution.__name__} passed all tests!')


if __name__ == '__main__':
    test_find_redundant_connection()
