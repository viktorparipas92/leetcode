"""
206. Reverse Linked List
------------------------
Difficulty: Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""


from linked_list.shared import ListNode, LinkedList


def reverse_linked_list(head: ListNode) -> ListNode:
    previous, current = None, head
    while current:
        next_node = current.next
        current.next = previous

        previous, current = current, next_node

    return previous


def test_reverse_linked_list():
    head = LinkedList([1, 2, 3, 4, 5]).head
    reversed_head = reverse_linked_list(head)
    assert reversed_head.val == 5
    assert reversed_head.next.val == 4
    assert reversed_head.next.next.val == 3
    assert reversed_head.next.next.next.val == 2
    assert reversed_head.next.next.next.next.val == 1
    assert reversed_head.next.next.next.next.next is None


if __name__ == '__main__':
    test_reverse_linked_list()