"""
21. Merge Two Sorted Lists
--------------------------
Difficulty: Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1 < list2:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    current.next = list1 or list2
    return dummy.next


def test_merge_two_lists():
    list1 = ListNode(
        1, ListNode(
            2, ListNode(
                4
            )
        )
    )
    list2 = ListNode(
        1, ListNode(
            3, ListNode(
                4
            )
        )
    )
    merged_list = merge_two_lists(list1, list2)
    assert merged_list.val == 1
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2
    assert merged_list.next.next.next.val == 3
    assert merged_list.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.next is None


if __name__ == '__main__':
    test_merge_two_lists()
