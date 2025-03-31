"""
25. Reverse Nodes in k-Group
----------------------------
Difficulty: Hard

You are given the head of a singly linked list head and a positive integer k.
You must reverse the first k nodes in the linked list,
and then reverse the next k nodes, and so on.
If there are fewer than k nodes left, leave the nodes as they are.
Return the modified list after reversing the nodes in each group of k.
You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:
Input: head = [1,2,3,4,5,6], k = 3
Output: [3,2,1,6,5,4]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The length of the linked list is n.
1 <= k <= n <= 100
0 <= Node.val <= 100
"""
from linked_list.shared import ListNode, LinkedList


def reverse_k_group_recursion(head: ListNode, k: int) -> ListNode:
    """
    Time complexity: O(n)
    Space complexity: O(n/k):
    """
    def reverse(first_node: ListNode, last_node: ListNode) -> tuple[ListNode, ListNode]:
        temporary_node = first_node.next
        first_node.next = last_node
        last_node = first_node
        first_node = temporary_node
        return first_node, last_node

    current_node = head
    current_group_size = 0
    while current_node and current_group_size < k:
        current_node = current_node.next
        current_group_size += 1

    if current_group_size == k:
        current_node = reverse_k_group_recursion(current_node, k)
        while current_group_size > 0:
            head, current_node = reverse(head, current_node)
            current_group_size -= 1

        head = current_node

    return head


def test_reverse_k_group():
    solutions = [
        reverse_k_group_recursion,
    ]

    test_cases = [
        ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ]

    for solution in solutions:
        for values, k, expected_output in test_cases:
            # Arrange
            head = LinkedList(values).head

            # Act
            new_head = solution(head, k)

            # Assert
            assert new_head == LinkedList(expected_output).head

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_reverse_k_group()
