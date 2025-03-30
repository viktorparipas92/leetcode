class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return other and self.val == other.val and self.next == other.next


class LinkedList:
    def __init__(self, underlying_list: list):
        self.head = None
        for element in underlying_list[::-1]:
            node = ListNode(element)
            node.next = self.head
            self.head = node
