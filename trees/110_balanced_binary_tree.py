"""
110. Balanced Binary Tree
-------------------------
Difficulty: Easy

Given a binary tree, determine if it is height-balanced.
"""

from typing import Optional

from trees.shared import TreeNode


def is_balanced(root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode]) -> tuple[int, bool]:
        if not node:
            return 0, True

        left_height, left_balanced = dfs(node.left)
        right_height, right_balanced = dfs(node.right)

        if (
            not left_balanced
            or not right_balanced
            or abs(left_height - right_height) > 1
        ):
            return 0, False

        return 1 + max(left_height, right_height), True

    return dfs(root)[1]


def test_is_balanced():
    tree = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )
    assert is_balanced(tree) is True

    tree = TreeNode(
        1,
        TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)),
        TreeNode(2),
    )
    assert is_balanced(tree) is False

    assert is_balanced(None) is True


if __name__ == '__main__':
    test_is_balanced()
