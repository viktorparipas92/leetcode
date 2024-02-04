"""
141. Linked List Cycle
-----------------------
Difficulty: Easy

Given head, the head of a linked list, determine if the linked list has a
cycle in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that
tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


from linked_list.shared import ListNode, LinkedList


def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


def test_has_cycle():
    head = LinkedList([3, 2, 0, -4]).head
    head.next.next.next.next = head.next  # pos = 1
    assert has_cycle(head) is True

    head = LinkedList([1, 2]).head
    head.next = head  # pos = 0
    assert has_cycle(head) is True

    head = LinkedList([1]).head
    assert has_cycle(head) is False


if __name__ == '__main__':
    test_has_cycle()
