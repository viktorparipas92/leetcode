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
from typing import Optional

from linked_list.shared import ListNode, LinkedList


def merge_k_lists_brute_force(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
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


def test_merge_k_lists():
    solutions = [
        merge_k_lists_brute_force,
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
