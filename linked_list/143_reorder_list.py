"""
143. Reorder List
-----------------
Difficulty: Medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

from linked_list.shared import ListNode, LinkedList


def reorder_list(head: ListNode) -> None:
    if not head or not head.next:
        return

    slow_node, fast_node = head, head
    while fast_node and fast_node.next:
        slow_node = slow_node.next  # will be at the middle of the list
        fast_node = fast_node.next.next  # will be at the end of the list

    previous_node, current_node = None, slow_node
    while current_node:  # reverse the second half of the list
        next_node = current_node.next
        current_node.next = previous_node

        # move to the next node
        previous_node, current_node = current_node, next_node

    first_node, second_node = head, previous_node
    while second_node.next:  # merge the two halves
        first_node.next, first_node = second_node, first_node.next
        second_node.next, second_node = first_node, second_node.next


def test_reorder_list():
    head = LinkedList([1, 2, 3, 4]).head
    reorder_list(head)
    assert head.val == 1
    assert head.next.val == 4
    assert head.next.next.val == 2
    assert head.next.next.next.val == 3

    head = LinkedList([1, 2, 3, 4, 5]).head
    reorder_list(head)
    assert head.val == 1
    assert head.next.val == 5
    assert head.next.next.val == 2
    assert head.next.next.next.val == 4
    assert head.next.next.next.next.val == 3