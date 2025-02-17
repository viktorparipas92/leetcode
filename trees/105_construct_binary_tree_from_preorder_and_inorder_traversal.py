"""
105. Construct Binary Tree from Preorder and Inorder Traversal
--------------------------------------------------------------
Difficulty: Medium

You are given two integer arrays preorder and inorder.
- preorder is the preorder traversal of a binary tree
- inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]

Example 2:
Input: preorder = [1], inorder = [1]
Output: [1]

Constraints:
1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
"""

from trees.shared import TreeNode as Node


def build_tree_dfs(preorder: list[int], inorder: list[int]) -> Node | None:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    if not preorder or not inorder:
        return

    root_value = preorder[0]
    root_node = Node(root_value)
    mid_index = inorder.index(root_value)
    root_node.left = build_tree_dfs(preorder[1: mid_index+1], inorder[:mid_index])
    root_node.right = build_tree_dfs(preorder[mid_index+1:], inorder[mid_index + 1:])
    return root_node


def build_tree_dfs_with_hash_map(preorder: list[int], inorder: list[int]) -> Node:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    inorder_indices: dict[int, int] = {value: i for i, value in enumerate(inorder)}
    preorder_index = 0

    def construct_tree(left_boundary: int, right_boundary: int) -> Node | None:
        nonlocal preorder_index
        if left_boundary > right_boundary:
            return

        root_value = preorder[preorder_index]
        root_node = Node(root_value)

        inorder_index = inorder_indices[root_value]

        preorder_index += 1

        root_node.left = construct_tree(left_boundary, inorder_index - 1)
        root_node.right = construct_tree(inorder_index + 1, right_boundary)
        return root_node

    return construct_tree(left_boundary=0, right_boundary=len(inorder) - 1)


def build_tree_dfs_optimal(preorder: list[int], inorder: list[int]) -> Node:
    """
    Time complexity: O(n)
    Space complexity: O(n)  # due to recursion stack
    """
    preorder_index = inorder_index = 0

    def construct_tree(limit: float | int) -> Node | None:
        nonlocal preorder_index, inorder_index
        if preorder_index >= len(preorder):
            return

        if inorder[inorder_index] == limit:
            inorder_index += 1
            return

        root_node = Node(preorder[preorder_index])

        preorder_index += 1

        root_node.left = construct_tree(root_node.value)
        root_node.right = construct_tree(limit)
        return root_node

    return construct_tree(limit=float('inf'))


def test_build_tree():
    solutions = [
        build_tree_dfs,
        build_tree_dfs_with_hash_map,
        build_tree_dfs_optimal,
    ]

    tree_1 = Node(1, Node(2), Node(3, None, Node(4)))
    tree_3 = Node(3, Node(9), Node(20, Node(15), Node(7)))
    test_cases = [
        ([1, 2, 3, 4], [2, 1, 3, 4], tree_1),
        ([1], [1], Node(1)),
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], tree_3),
    ]

    for solution in solutions:
        for preorder, inorder, expected_tree in test_cases:
            # Act
            tree = solution(preorder, inorder)

            # Assert
            assert list(tree.preorder()) == preorder
            assert list(tree.inorder()) == inorder

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_build_tree()
