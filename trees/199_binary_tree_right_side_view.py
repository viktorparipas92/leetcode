"""
199. Binary Tree Right Side View
---------------------------------
Difficulty: Medium

You are given the root of a binary tree. Return only the values of the nodes that are
visible from the right side of the tree, ordered from top to bottom.

Example 1:
Input: root = [1,2,3]
Output: [1,3]
Example 2:

Input: root = [1,2,3,4,5,6,7]
Output: [1,3,7]

Constraints:
0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""
from collections import deque

from trees.shared import TreeNode


def right_side_view_dfs(root: TreeNode) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    nodes_on_the_right = []

    def depth_first_search(node: TreeNode, depth: int):
        if not node:
            return None

        if depth == len(nodes_on_the_right):
            nodes_on_the_right.append(node.value)

        depth_first_search(node.right, depth + 1)
        depth_first_search(node.left, depth + 1)

    depth_first_search(root, depth=0)
    return nodes_on_the_right


def right_side_view_bfs(root: TreeNode) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    nodes_on_the_right = []
    node_queue = deque([root])
    while node_queue:
        right_side = None
        
        queue_length = len(node_queue)
        for i in range(queue_length):
            if node := node_queue.popleft():
                right_side = node
                node_queue.append(node.left)
                node_queue.append(node.right)

        if right_side:
            nodes_on_the_right.append(right_side.value)

    return nodes_on_the_right


def test_right_side_view():
    solutions = [
        right_side_view_dfs,
        right_side_view_bfs,
    ]

    tree_1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree_2 = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
    )
    tree_3 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    tree_4 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
    test_cases = [
        (tree_1, [1, 3]),
        (tree_2, [1, 3, 7]),
        (tree_3, [1, 3, 4]),
        (tree_4, [1, 3, 4, 5]),
    ]

    for solution in solutions:
        for tree, expected_right_side in test_cases:
            # Act
            right_side = solution(tree)

            # Assert
            assert right_side == expected_right_side

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_right_side_view()
