"""
226. Invert Binary Tree
-----------------------
Difficulty: Easy

Given the root of a binary tree, invert the tree, and return its root.
"""
from typing import Optional

from trees.shared import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def test_invert_tree():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted_tree = invert_tree(root)
    assert inverted_tree.value == 4
    assert inverted_tree.left.value == 7
    assert inverted_tree.right.value == 2
    assert inverted_tree.left.left.value == 9
    assert inverted_tree.left.right.value == 6
    assert inverted_tree.right.left.value == 3
    assert inverted_tree.right.right.value == 1

    root = None
    inverted_tree = invert_tree(root)
    assert inverted_tree is None

