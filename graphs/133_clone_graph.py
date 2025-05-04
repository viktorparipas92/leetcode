"""
133. Clone Graph
----------------
Difficulty: Medium

Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list.
An adjacency list is a mapping of nodes to lists, used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n,
where n is the total number of nodes in the graph.
The index of each node within the adjacency list is the same as the node's value
(1-indexed).
The input node will always be the first node in the graph and have 1 as the value.

Example 1:
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: The graph is empty.

Constraints:
0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
"""
from typing import Optional

from graphs.shared import Node


def clone_graph_dfs(node: Optional[Node]) -> Optional[Node]:
    """
    Time complexity: O(v + e)
    Space complexity: O(v)
    where v is the number of vertices and e is the number of edges in the graph.
    """
    def depth_first_search(node: Node) -> Node:
        if node in node_mapping:
            return node_mapping[node]

        node_copy = Node(node.value)
        node_mapping[node] = node_copy
        for neighbour in node.neighbours:
            node_copy.neighbours.append(depth_first_search(neighbour))

        return node_copy

    node_mapping: dict = {}
    return depth_first_search(node) if node else None


def test_clone_graph():
    solutions = [
        clone_graph_dfs,
    ]

    node_11 = Node(1)
    node_12 = Node(2, neighbours=[node_11])
    node_11.neighbours = [node_12]
    node_13 = Node(3, neighbours=[node_12])
    node_12.neighbours.append(node_13)

    node_21 = Node(1)

    test_cases = [
        (node_11, [[2], [1, 3], [2]]),
        (node_21, [[]]),
        (None, []),
    ]

    for solution in solutions:
        for graph, adjacency_list in test_cases:
            # Act
            cloned_graph = solution(graph)

            # Assert
            assert cloned_graph == graph

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_clone_graph()
