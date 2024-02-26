"""
104. Maximum Depth of Binary Tree
---------------------------------
Difficulty: Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.
"""
from typing import Optional

from trees.shared import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


def test_max_depth():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3

    root = TreeNode(1, TreeNode(2), None)
    assert max_depth(root) == 2

    root = None
    assert max_depth(root) == 0
