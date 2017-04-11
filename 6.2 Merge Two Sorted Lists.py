class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        node = dummy
        n1, n2 = l1, l2
        while n1 and n2:
            if n1.val < n2.val:
                node.next = n1
                n1 = n1.next
            else:
                node.next = n2
                n2 = n2.next
            node = node.next
        if n1:
            node.next = n1
        else:
            node.next = n2
        return dummy.next


l1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
l2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))

inst = Solution()
head = inst.mergeTwoLists(l1, l2)

while head:
    print(head.val, end=' ')
    head = head.next
print()
