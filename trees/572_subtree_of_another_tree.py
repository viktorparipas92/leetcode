"""
572. Subtree of Another Tree
----------------------------
Difficulty: Easy

Given the roots of two binary trees root and subRoot, return true
if there is a subtree of root with the same structure
and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all
of this node's descendants.
The tree could also be considered as a subtree of itself.
"""

from trees.shared import TreeNode, is_same_tree


def is_subtree(root: TreeNode, sub_root: TreeNode) -> bool:
    if root is None:
        return False

    if is_same_tree(root, sub_root):
        return True

    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


def test_is_subtree():
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(root, sub_root) is True

    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(root, sub_root) is False

