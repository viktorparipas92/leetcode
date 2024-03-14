"""
100. Same Tree
--------------
Difficulty: Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
"""
from trees.shared import TreeNode, is_same_tree


def test_is_same_tree():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p, q) is True

    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p, q) is False

    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert is_same_tree(p, q) is False
