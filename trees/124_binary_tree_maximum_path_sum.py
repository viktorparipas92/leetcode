"""
124. Binary Tree Maximum Path Sum
---------------------------------
Difficulty: Hard

Given the root of a non-empty binary tree, return the maximum path sum of
any non-empty path.
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has
an edge connecting them. A node can not appear in the sequence more than once.
The path does not necessarily need to include the root.
The path sum of a path is the sum of the node's values in the path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:
1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""
from typing import Optional

from trees.shared import TreeNode


def max_path_sum_dfs(root: TreeNode) -> int | float:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    max_sum = -float('inf')

    def depth_first_search(root: Optional[TreeNode]):
        if root is None:
            return

        nonlocal max_sum
        left = get_maximum(root.left)
        right = get_maximum(root.right)
        max_sum = max(max_sum, root.value + left + right)
        depth_first_search(root.left)
        depth_first_search(root.right)

    depth_first_search(root)
    return max_sum


def get_maximum(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    left = get_maximum(root.left)
    right = get_maximum(root.right)
    path = root.value + max(left, right)
    return max(0, path)


def test_max_path_sum():
    solutions = [
        max_path_sum_dfs,
    ]

    test_cases = [
        (TreeNode(1, TreeNode(2), TreeNode(3)), 6),
        (TreeNode(-15, TreeNode(10), TreeNode(20, TreeNode(15), TreeNode(5, TreeNode(-5)))), 40),
    ]

    for solution in solutions:
        for root_node, expected_max_path_sum in test_cases:
            # Act
            max_path_sum = solution(root_node)

            # Assert
            assert max_path_sum == expected_max_path_sum

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_max_path_sum()



