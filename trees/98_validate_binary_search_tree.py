"""
98. Validate Binary Search Tree
-------------------------------
Difficulty: Medium

Given the root of a binary tree, return true if it is a valid binary search tree,
otherwise return false.

A valid binary search tree satisfies the following constraints:
- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the
node's key.
- Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [1,2,3]
Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

Constraints:
1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""

from trees.shared import TreeNode

left_check = staticmethod(lambda val, limit: val < limit)
right_check = staticmethod(lambda val, limit: val > limit)


def is_valid_bst_brute_force(root: TreeNode) -> bool:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    if not root:
        return True

    if (
        not is_valid(root.left, root.value, left_check)
        or not is_valid(root.right, root.value, right_check)
    ):
        return False

    return (
        is_valid_bst_brute_force(root.left)
        and is_valid_bst_brute_force(root.right)
    )


def is_valid_bst_depth_first(root: TreeNode) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def is_valid(node: TreeNode, left: int | float, right: int | float) -> bool:
        if not node:
            return True

        if not (left < node.value < right):
            return False

        return (
            is_valid(node.left, left=left, right=node.value)
            and is_valid(node.right, left=node.value, right=right)
        )

    return is_valid(root, left=float('-inf'), right=float('inf'))


def is_valid(root: TreeNode | None, limit: int, check: callable) -> bool:
    if not root:
        return True
    elif not check(root.value, limit):
        return False

    return is_valid(root.left, limit, check) and is_valid(root.right, limit, check)


def test_is_valid_bst():
    solutions = [
        is_valid_bst_brute_force,
        is_valid_bst_depth_first,
    ]

    test_cases = [
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),
        (TreeNode(1, TreeNode(2), TreeNode(3)), False),
        (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
    ]

    for solution in solutions:
        for root_node, expected_is_valid_bst in test_cases:
            # Act
            is_valid_bst = solution(root_node)

            # Assert
            assert is_valid_bst == expected_is_valid_bst

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_is_valid_bst()
