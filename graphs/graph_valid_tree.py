"""
Graph Valid Tree
================
Difficulty: Medium

Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check
whether these edges make up a valid tree.

Example 1:
Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true

Example 2:
Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false

Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0]
and thus will not appear together in edges.

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""


def valid_tree_cycle_detection_dfs(n: int, edges: list[list[int]]) -> bool:
    """
    Time complexity: O(V + E)
    Space complexity: O(V + E)
    where V is the number of vertices (nodes) and E is the number of edges.
    """
    def depth_first_search(node: int, parent: int) -> bool:
        if node in visited_nodes:
            return False

        visited_nodes.add(node)
        for neighbor in adjacency_list[node]:
            if neighbor == parent:
                continue

            if not depth_first_search(neighbor, node):
                return False

        return True

    num_nodes = n
    if len(edges) > (num_nodes - 1):
        return False

    adjacency_list: list[list[int]] = [[] for _ in range(num_nodes)]
    for node_1, node_2 in edges:
        adjacency_list[node_1].append(node_2)
        adjacency_list[node_2].append(node_1)

    visited_nodes = set()
    return depth_first_search(node=0, parent=-1) and len(visited_nodes) == num_nodes


def test_valid_tree():
    solutions = [
        valid_tree_cycle_detection_dfs,
    ]

    test_cases = [
        ((5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True),
        ((5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False),
    ]

    for solution in solutions:
        for (num_nodes, edges), expected_is_valid in test_cases:
            # Act
            is_valid = solution(num_nodes, edges)

            # Assert
            assert is_valid == expected_is_valid

        print(f'{solution.__name__} passed all tests!')


if __name__ == '__main__':
    test_valid_tree()
