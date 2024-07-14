"""
19. Remove Nth Node From End of List
------------------------------------
Difficulty: Medium

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.
"""

from linked_list.shared import ListNode, LinkedList


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(next=head)
    left = right = dummy
    for _ in range(n + 1):
        right = right.next

    while right:
        left, right = left.next, right.next

    left.next = left.next.next
    return dummy.next


def remove_nth_from_end_2(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


def test_remove_nth_from_end():
    head = LinkedList([1, 2, 3, 4, 5]).head
    new_head = remove_nth_from_end(head, 2)
    assert new_head.val == 1
    assert new_head.next.val == 2
    assert new_head.next.next.val == 3
    assert new_head.next.next.next.val == 5
    assert new_head.next.next.next.next is None