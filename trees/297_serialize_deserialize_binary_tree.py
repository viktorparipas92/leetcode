"""
297. (De)/serialize a binary tree
--------------------------------
Difficulty: Hard

Implement an algorithm to serialize and deserialize a binary tree.
Serialization is the process of converting an in-memory structure into a sequence of
bits so that it can be stored or sent across a network to be reconstructed later
in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this
string can be deserialized to the original tree structure.
There is no additional restriction on how your serialization/deserialization
algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes
a binary tree. You do not necessarily need to follow this format.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""
from collections import deque
from typing import Optional

from trees.shared import TreeNode


class Codec:
    DELIMITER = ','
    NULL = 'null'

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        pass


class CodecDFS(Codec):
    """
    Both methods have a time complexity of O(n) and a space complexity of O(n).
    """
    def serialize(self, root: Optional[TreeNode]) -> str:
        def depth_first_search(node: Optional[TreeNode]):
            if node is None:
                nodes.append(self.NULL)
                return

            nodes.append(str(node.value))
            depth_first_search(node.left)
            depth_first_search(node.right)

        nodes: list = []
        depth_first_search(root)
        return self.DELIMITER.join(nodes)

    def deserialize(self, tree_data: str) -> Optional[TreeNode]:
        def depth_first_search() -> Optional[TreeNode]:
            nonlocal index
            if nodes[index] == self.NULL:
                index += 1
                return

            node = TreeNode(int(nodes[index]))
            index += 1
            node.left = depth_first_search()
            node.right = depth_first_search()
            return node

        nodes: list[str] = tree_data.split(self.DELIMITER)
        index = 0
        return depth_first_search()


class CodecBFS(Codec):
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''

        nodes: list = []
        queue: deque = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                nodes.append(self.NULL)
                continue

            nodes.append(str(node.value))
            queue.append(node.left)
            queue.append(node.right)

        while nodes and nodes[-1] == self.NULL:
            nodes.pop()

        return self.DELIMITER.join(nodes)

    def deserialize(self, tree_data: str) -> Optional[TreeNode]:
        nodes: list[str] = tree_data.split(self.DELIMITER)
        if not nodes:
            return

        first_node: str = nodes[0]
        if first_node == self.NULL or not first_node:
            return

        root = TreeNode(int(first_node))
        queue: deque[TreeNode] = deque([root])
        index = 1
        while queue and index < len(nodes):
            node = queue.popleft()
            serialized_node: str = nodes[index]
            if serialized_node != self.NULL:
                node.left = TreeNode(int(serialized_node))
                queue.append(node.left)

            index += 1
            serialized_node: str = nodes[index]
            if serialized_node != self.NULL:
                node.right = TreeNode(int(serialized_node))
                queue.append(node.right)

            index += 1

        return root


def test_serialize_deserialize():
    solutions = [
        # CodecDFS(),
        CodecBFS(),
    ]

    test_cases = [
        (TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))), '1,2,3,null,null,4,5'),
        (None, ''),
    ]

    for solution in solutions:
        for root_node, expected_serialization in test_cases:
            # Act
            serialized_tree = solution.serialize(root_node)

            # Assert
            assert serialized_tree == expected_serialization

            # Act
            deserialized_tree = solution.deserialize(serialized_tree)

            # Assert
            assert deserialized_tree == root_node

        print(f'Tests passed for {solution.__class__.__name__}!')


if __name__ == '__main__':
    test_serialize_deserialize()
