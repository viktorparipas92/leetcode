"""
230. K-th Smallest Element in a Binary Search Tree
---------------------------------------------------
Difficulty: Medium

Given the root of a binary search tree, and an integer k, return the k-th smallest
value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:
- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the
  node's key.
- Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3], k = 1
Output: 1

Example 2:
Input: root = [4,3,5,2,null], k = 4
Output: 5

Constraints:
1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000
"""


from trees.shared import TreeNode


def kth_smallest_dfs_recursive_preorder_sorting(root: TreeNode | None, k: int) -> int:
    """
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    node_values = []

    def depth_first_search(node: TreeNode):
        if not node:
            return

        node_values.append(node.value)
        depth_first_search(node.left)
        depth_first_search(node.right)

    depth_first_search(root)
    node_values.sort()
    return node_values[k - 1]


def kth_smallest_dfs_recursive_inorder(root: TreeNode | None, k: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    node_values = []

    def depth_first_search(node: TreeNode):
        if not node:
            return

        depth_first_search(node.left)
        node_values.append(node.value)
        depth_first_search(node.right)

    depth_first_search(root)
    return node_values[k - 1]


def kth_smallest_dfs_recursive_inorder_optimal(root: TreeNode | None, k: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)  # due to recursion stack
    """
    count = 0
    kth_smallest = root.value

    def depth_first_search(node: TreeNode):
        nonlocal count, kth_smallest
        if not node:
            return

        depth_first_search(node.left)
        count += 1
        if count == k:
            kth_smallest = node.value
            return

        depth_first_search(node.right)

    depth_first_search(root)
    return kth_smallest


def kth_smallest_dfs_iterative_inorder(root: TreeNode | None, k: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    node_stack: list[TreeNode] = []
    current_node = root
    while node_stack or current_node:
        while current_node:
            node_stack.append(current_node)
            current_node = current_node.left

        current_node = node_stack.pop()
        k -= 1
        if k == 0:
            return current_node.value

        current_node = current_node.right


def kth_smallest_dfs_morris_inorder(root: TreeNode | None, k: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    current_node = root
    while current_node:
        if not current_node.left:
            k -= 1
            if k == 0:
                return current_node.value

            current_node = current_node.right
        else:  # current_node.left exists
            predecessor = current_node.left
            while predecessor.right and predecessor.right != current_node:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = current_node
                current_node = current_node.left
            else:
                predecessor.right = None
                k -= 1
                if k == 0:
                    return current_node.value

                current_node = current_node.right

    return -1


def test_kth_smallest():
    solutions = [
        kth_smallest_dfs_recursive_preorder_sorting,
        kth_smallest_dfs_recursive_inorder,
        kth_smallest_dfs_recursive_inorder_optimal,
        kth_smallest_dfs_iterative_inorder,
        kth_smallest_dfs_morris_inorder,
    ]

    tree_4 = TreeNode(
        5,
        TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
        TreeNode(6),
    )
    test_cases = [
        ([TreeNode(2, TreeNode(1), TreeNode(3)), 1], 1),
        ([TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(5)), 4], 5),
        ([TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1], 1),
        ([tree_4, 3], 3),
    ]

    for solution in solutions:
        for (root, k), expected_kth_smallest in test_cases:
            # Act
            kth_smallest = solution(root, k)

            # Assert
            assert kth_smallest == expected_kth_smallest

        print(f'All tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_kth_smallest()
