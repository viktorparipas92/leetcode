"""
2. Add Two Numbers
-------------------
Difficulty: Medium

You are given two non-empty linked lists, l1 and l2, where each represents a
non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as
3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional

from linked_list.shared import ListNode, LinkedList


def add_recursive(
    list_1: Optional[ListNode], list_2: Optional[ListNode], carry: int
) -> Optional[ListNode]:
    if not list_1 and not list_2 and carry == 0:
        return

    value_1 = list_1.val if list_1 else 0
    value_2 = list_2.val if list_2 else 0

    carry, value = divmod(value_1 + value_2 + carry, 10)
    next_node = add_recursive(
        list_1.next if list_1 else None,
        list_2.next if list_2 else None,
        carry,
    )
    return ListNode(value, next_node)


def add_two_numbers(
    list_1: Optional[ListNode], list_2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Solution with recursion.
    Time complexity: O(m + n), where m and n are the lengths of the linked lists.
    Space complexity: O(m + n), where m and n are the lengths of the linked lists.
    """
    return add_recursive(list_1, list_2, 0)


def test_case_1(method_under_test):
    # Arrange
    list_1 = LinkedList([1, 2, 3])
    list_2 = LinkedList([4, 5, 6])

    # Act
    result = add_two_numbers(list_1.head, list_2.head)

    # Assert
    assert result.val == 5
    assert result.next.val == 7
    assert result.next.next.val == 9


def test_case_2(method_under_test):
    # Arrange
    list_1 = LinkedList([9])
    list_2 = LinkedList([9])

    # Act
    result = method_under_test(list_1.head, list_2.head)

    # Assert
    assert result.val == 8
    assert result.next.val == 1




if __name__ == "__main__":
    methods = [
        add_two_numbers,
    ]

    for solution in methods:
        test_case_1(solution)
        test_case_2(solution)
        print(f"All tests passed for {solution.__name__}")
