"""
Number of Connected Components in an Unconnected Graph
--------------------------------------------------------
Difficulty: Medium

There is an undirected graph with n nodes.
There is also an edges array, where edges[i] = [a, b] means
that there is an edge between node a and node b in the graph.
The nodes are numbered from 0 to n - 1.
Return the total number of connected components in that graph.

Example 1:
Input: n=3, edges=[[0,1], [0,2]]
Output: 1

Example 2:
Input: n=6, edges=[[0,1], [1,2], [2,3], [4,5]]
Output: 2

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""
from collections import deque


def count_components_dfs(n: int, edges: list[list[int]]) -> int:
    """
    Time complexity: O(V + E)
    Space complexity: O(V + E)
    """
    def depth_first_seach(node: int):
        for neighbor in adjacency_list[node]:
            if not visited_nodes[neighbor]:
                visited_nodes[neighbor] = True
                depth_first_seach(neighbor)

    adjacency_list: list[list[int]] = [[] for _ in range(n)]

    num_nodes: int = n
    visited_nodes: list[bool] = [False] * num_nodes
    for node_1, node_2 in edges:
        adjacency_list[node_1].append(node_2)
        adjacency_list[node_2].append(node_1)

    component_count: int = 0
    for node in range(num_nodes):
        if not visited_nodes[node]:
            visited_nodes[node] = True
            depth_first_seach(node)
            component_count += 1

    return component_count


def count_components_bfs(n: int, edges: list[list[int]]) -> int:
    """
    Time complexity: O(V + E)
    Space complexity: O(V + E)
    """
    def breadth_first_search(node: int):
        queue = deque([node])
        visited_nodes[node] = True
        while queue:
            current_node = queue.popleft()
            for neighbor in adjacency_list[current_node]:
                if not visited_nodes[neighbor]:
                    visited_nodes[neighbor] = True
                    queue.append(neighbor)

    adjacency_list: list[list[int]] = [[] for _ in range(n)]

    num_nodes: int = n
    visited_nodes: list[bool] = [False] * num_nodes
    for node_1, node_2 in edges:
        adjacency_list[node_1].append(node_2)
        adjacency_list[node_2].append(node_1)

    component_count: int = 0
    for node in range(num_nodes):
        if not visited_nodes[node]:
            breadth_first_search(node)
            component_count += 1

    return component_count


def test_count_components():
    solutions = [
        count_components_dfs,
        count_components_bfs,
    ]

    test_cases = [
        (3, [[0, 1], [0, 2]], 1),
        (6, [[0, 1], [1, 2], [2, 3], [4, 5]], 2),
    ]

    for solution in solutions:
        for num_nodes, edges, expected_component_count in test_cases:
            # Act
            component_count = solution(num_nodes, edges)

            # Assert
            assert component_count == expected_component_count

        print(f'{solution.__name__} passed all tests!')


if __name__ == '__main__':
    test_count_components()
