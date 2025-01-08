"""
138. Copy Linked List with Random Pointer
-----------------------------------------
Difficulty: Medium

You are given the head of a linked list of length n.

Unlike a singly linked list, each node contains an additional pointer random,
which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:
- The original value val of the copied node
- A next pointer to the new node corresponding to the next pointer of the original node
- A random pointer to the new node corresponding to the random pointer of the
original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes.
Each node is represented as a pair of [val, random_index]
where random_index is the index of the node (0-indexed) that the random pointer points
to, or null if it does not point to any node.

Example 1:
Input: head = [[3,null],[7,3],[4,0],[5,1]]
Output: [[3,null],[7,3],[4,0],[5,1]]

Example 2:
Input: head = [[1,null],[2,2],[3,2]]
Output: [[1,null],[2,2],[3,2]]
Constraints:

0 <= n <= 100
-100 <= Node.val <= 100
random is null or is pointing to some node in the linked list.

"""
from collections import defaultdict


class NodeWithRandom:
    def __init__(
        self,
        val: int = 0,
        next_: 'ListNodeWithRandom | None' = None,
        random: 'ListNodeWithRandom | None' = None,
    ):
        self.val = val
        self.next = next_
        self.random = random

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


class LinkedListWithRandom:
    def __init__(self, nodes: list[tuple[int, int | None]]):
        self.head = None
        if not nodes:
            return

        node_list = [NodeWithRandom(val) for val, _ in nodes]
        self.head = node_list[0]

        for i, (val, random_index) in enumerate(nodes):
            if i < len(nodes) - 1:
                node_list[i].next = node_list[i + 1]

            if random_index is not None:
                node_list[i].random = node_list[random_index]

        self.head = node_list[0]


class Solution:
    def __init__(self):
        self.map = {}

    def copy_random_list_with_recursion(
        self, head: 'NodeWithRandom | None'
    ) -> 'NodeWithRandom | None':
        if head is None:
            return
        elif head in self.map:
            return self.map[head]

        copy = NodeWithRandom(head.val)
        self.map[head] = copy
        copy.next = self.copy_random_list_with_recursion(head.next)
        copy.random = self.map.get(head.random)
        return copy

    @staticmethod
    def copy_random_list_with_two_pass(
        head: 'NodeWithRandom | None'
    ) -> 'NodeWithRandom | None':
        old_to_copy = {None: None}

        current = head
        while current:
            copy = NodeWithRandom(current.val)
            old_to_copy[current] = copy
            current = current.next

        current = head
        while current:
            copy = old_to_copy[current]
            copy.next = old_to_copy[current.next]
            copy.random = old_to_copy[current.random]
            current = current.next

        return old_to_copy[head]

    @staticmethod
    def copy_random_list_with_one_pass(
        head: 'NodeWithRandom | None'
    ) -> 'NodeWithRandom | None':
        old_to_copy = defaultdict(lambda: NodeWithRandom(0))
        old_to_copy[None] = None

        current = head
        while current:
            old_to_copy[current].val = current.val
            old_to_copy[current].next = old_to_copy[current.next]
            old_to_copy[current].random = old_to_copy[current.random]
            current = current.next

        return old_to_copy[head]

    @staticmethod
    def copy_random_list_space_optimized(
        head: 'NodeWithRandom | None'
    ) -> 'NodeWithRandom | None':
        if head is None:
            return

        current = head
        while current:
            new_node = NodeWithRandom(current.val)
            new_node.next = current.random

            current.random = new_node
            current = current.next

        new_head = head.random
        current = head
        while current:
            new_node = current.random
            new_node.random = new_node.next.random if new_node.next else None
            current = current.next

        current = head
        while current is not None:
            new_node = current.random
            current.random = new_node.next
            new_node.next = current.next.random if current.next else None
            current = current.next

        return new_head


def test_copy_random_list():
    node_list = [(3, None), (7, 3), (4, 0), (5, 1)]
    head = LinkedListWithRandom(node_list).head

    solution = Solution()
    solutions = [
        solution.copy_random_list_with_recursion,
        solution.copy_random_list_with_two_pass,
        solution.copy_random_list_with_one_pass,
        solution.copy_random_list_space_optimized,
    ]
    for copy_function in solutions:
        copied_head = copy_function(head)

        assert copied_head.val == 3
        assert copied_head.random is None

        assert copied_head.next.val == 7
        assert copied_head.next.random.val == node_list[3][0]

        assert copied_head.next.next.val == 4
        assert copied_head.next.next.random.val == node_list[0][0]

        assert copied_head.next.next.next.val == 5
        assert copied_head.next.next.next.random.val == node_list[1][0]


if __name__ == '__main__':
    test_copy_random_list()