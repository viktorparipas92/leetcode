"""
235. Lowest Common Ancestor of a Binary Search Tree
-----------------------------------------------------
Difficulty: Medium

Given a binary search tree (BST) where all node values are unique, and two nodes from
the tree are p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T
such that both p and q as descendants. The ancestor is allowed to be a descendant of
itself.

Constraints:

2 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST.
"""

from trees.shared import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    With recursion.
    Time complexity: O(h), space complexity: O(h), where h is the height of the tree.
    """
    if max(p.value, q.value) < root.value:
        return lowest_common_ancestor(root.left, p, q)

    elif min(p.value, q.value) > root.value:
        return lowest_common_ancestor(root.right, p, q)

    return root


def lowest_common_ancestor_iterative(
    root: TreeNode, p: TreeNode, q: TreeNode
) -> TreeNode:
    """
    With iteration.
    Time complexity: O(h), space complexity: O(1), where h is the height of the tree.
    """
    current = root
    while current:
        if max(p.value, q.value) < current.value:
            current = current.left
        elif min(p.value, q.value) > current.value:
            current = current.right
        else:
            return current


def test_lowest_common_ancestor_of_binary_search_tree():
    solutions = [
        lowest_common_ancestor,
        lowest_common_ancestor_iterative,
    ]
    tree = TreeNode(
        5,
        TreeNode(3, TreeNode(1, TreeNode(2)), TreeNode(4)),
        TreeNode(8, TreeNode(7), TreeNode(9))
    )
    p, q = TreeNode(3), TreeNode(8)
    assert lowest_common_ancestor(tree, p, q).value == 5
    assert lowest_common_ancestor_iterative(tree, p, q).value == 5

    p, q = TreeNode(3), TreeNode(4)
    assert lowest_common_ancestor(tree, p, q).value == 3
    assert lowest_common_ancestor_iterative(tree, p, q).value == 3


if __name__ == '__main__':
    test_lowest_common_ancestor_of_binary_search_tree()