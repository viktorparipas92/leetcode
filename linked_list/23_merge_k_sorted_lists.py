"""
23. Merge k Sorted Lists
------------------------------
Difficulty: Hard

You are given an array of k linked lists, where each list is sorted in ascending order.
Return the sorted linked list that is the result of merging all of the individual
linked lists.

Example 1:
Input: lists = [[1,2,4],[1,3,5],[3,6]]
Output: [1,1,2,3,3,4,5,6]

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000
"""
import heapq
from typing import Optional

from linked_list.shared import ListNode, LinkedList


def merge_k_lists_brute_force(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time complexity: O(n * log(n))
    Space complexity: O(n)
    """
    nodes = []
    for list_node in lists:
        while list_node:
            nodes.append(list_node.val)
            list_node = list_node.next

    nodes.sort()

    merged_node = ListNode(0)
    current_node = merged_node
    for node in nodes:
        current_node.next = ListNode(node)
        current_node = current_node.next

    return merged_node.next


def merge_k_lists_heap(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time complexity: O(n * log(k))
    Space complexity: O(k)
    """
    if not lists:
        return

    merged_node = ListNode(0)
    current_node = merged_node
    node_heap = []

    for list_node in lists:
        if list_node is not None:
            heapq.heappush(node_heap, list_node)

    while node_heap:
        popped_node = heapq.heappop(node_heap)
        current_node.next = popped_node
        current_node = current_node.next

        if popped_node.next:
            heapq.heappush(node_heap, popped_node.next)

    return merged_node.next


def merge_k_lists_divide_and_conquer_recursive(
    lists: list[Optional[ListNode]]
) -> Optional[ListNode]:
    """
    Time complexity: O(n * log(k))
    Space complexity: O(log(k))
    """
    if not lists:
        return

    length = len(lists)
    return divide(lists, left=0, right=length - 1)


def divide(
    lists: list[Optional[ListNode]], *, left: int, right: int
) -> Optional[ListNode]:
    if left > right:
        return
    elif left == right:
        return lists[left]

    middle = left + (right - left) // 2
    left_node = divide(lists, left=left, right=middle)
    right_node = divide(lists, left=middle + 1, right=right)
    return conquer(left_node, right_node)


def conquer(
    node_1: Optional[ListNode], node_2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy_node = ListNode(0)
    current_node = dummy_node

    while node_1 and node_2:
        if node_1 <= node_2:
            current_node.next = node_1
            node_1 = node_1.next
        else:
            current_node.next = node_2
            node_2 = node_2.next

        current_node = current_node.next

    current_node.next = node_1 or node_2
    return dummy_node.next


def test_merge_k_lists():
    solutions = [
        merge_k_lists_brute_force,
        merge_k_lists_heap,
        merge_k_lists_divide_and_conquer_recursive,
    ]

    test_cases = [
        ([[1, 2, 4], [1, 3, 5], [3, 6]], [1, 1, 2, 3, 3, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ]

    for solution in solutions:
        for lists, expected_merged_list in test_cases:
            # Arrange
            lists = [LinkedList(_list).head for _list in lists]

            # Act
            merged_list_node = solution(lists)

            # Assert
            expected_merged_list_node = LinkedList(expected_merged_list).head
            assert merged_list_node == expected_merged_list_node

        print(f'Tests passed for {solution.__name__}!')


if __name__ == '__main__':
    test_merge_k_lists()
