"""
1448. Count Good Nodes in Binary Tree
-------------------------------------
Difficulty: Medium

Within a binary tree, a node x is considered good if the path from the root of the tree
to the node x contains no nodes with a value greater than the value of node x.

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:
Input: root = [2,1,1,3,null,1,5]
Output: 3

Example 2:
Input: root = [1,2,-1,3,4]
Output: 4

Constraints:
1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""
from trees.shared import TreeNode


def good_nodes_dfs(root: TreeNode) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def depth_first_search(node, maximum_value):
        if not node:
            return 0

        if node.value >= maximum_value:
            maximum_value = node.value
            num_good_nodes = 1
        else:
            num_good_nodes = 0

        num_good_nodes += depth_first_search(node.left, maximum_value)
        num_good_nodes += depth_first_search(node.right, maximum_value)
        return num_good_nodes

    return depth_first_search(root, root.value)


def test_good_nodes():
    solutions = [
        good_nodes_dfs,
    ]

    tree_1 = TreeNode(
        2, TreeNode(1, TreeNode(3)), TreeNode(1, TreeNode(1), TreeNode(5))
    )
    tree_3 = TreeNode(
        3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5))
    )
    test_cases = [
        (tree_1, 3),
        (TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(-1)), 4),
        (tree_3, 4),
        (TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2))), 3),
    ]

    for solution in solutions:
        for tree, expected_num_good_nodes in test_cases:
            # Act
            num_good_nodes = solution(tree)

            # Assert
            assert num_good_nodes == expected_num_good_nodes

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_good_nodes()
