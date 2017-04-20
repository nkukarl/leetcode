class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1, l2):
        n1, n2 = l1, l2
        carry = 0
        mark = ListNode(0)
        n = mark
        while n1 is not None or n2 is not None:
            v1 = n1.val if n1 is not None else 0
            v2 = n2.val if n2 is not None else 0
            result = v1 + v2 + carry
            val = result % 10
            carry = result // 10
            n.next = ListNode(val)
            if n1 is not None:
                n1 = n1.next
            if n2 is not None:
                n2 = n2.next
            n = n.next
        if carry:
            n.next = ListNode(1)

        return mark.next
