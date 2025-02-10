"""
102. Binary Tree Level Order Traversal
---------------------------------------
Difficulty: Medium

Given a binary tree root, return the level-order traversal of it as a nested list,
where each sublist contains the values of nodes at a particular level in the tree,
from left to right.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in both trees <= 1000.
-1000 <= Node.val <= 1000
"""


from shared import TreeNode


def level_order_traversal_dfs(root: TreeNode) -> list[list[int]]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    level_values: list[list[int]] = []

    def traverse_tree(node: TreeNode, current_depth: int):
        """
        Traverse the tree in a depth-first manner.
        """
        if not node:
            return None

        if len(level_values) == current_depth:
            level_values.append([])

        level_values[current_depth].append(node.value)

        traverse_tree(node.left, current_depth + 1)
        traverse_tree(node.right, current_depth + 1)

    traverse_tree(root, current_depth=0)
    return level_values


def test_level_order_traversal():
    solutions = [
        level_order_traversal_dfs,
    ]

    tree_1 = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    test_cases = [
        (tree_1, [[1], [2, 3], [4, 5, 6, 7]]),
        (TreeNode(1), [[1]]),
        (None, []),
    ]

    for solution in solutions:
        for tree, nodes_in_expected_order in test_cases:
            # Act
            nodes_in_order = solution(tree)

            # Assert
            assert nodes_in_order == nodes_in_expected_order

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_level_order_traversal()
