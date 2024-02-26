"""
543. Diameter of Binary Tree
----------------------------
Difficulty: Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.
"""
from typing import Optional

from trees.shared import TreeNode


def diameter_of_binary_tree(root: TreeNode) -> int:
    def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
        if not node:
            max_height = max_diameter = 0
        else:
            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            max_height = 1 + max(left_height, right_height)
            max_diameter = max(
                left_diameter, right_diameter, left_height + right_height
            )

        return max_height, max_diameter

    return dfs(root)[1]


def test_diameter_of_binary_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter_of_binary_tree(root) == 3

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert diameter_of_binary_tree(root) == 1

    root = TreeNode(1, TreeNode(2))
    assert diameter_of_binary_tree(root) == 1
