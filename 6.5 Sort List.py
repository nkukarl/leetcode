class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        fast, slow = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        L, R = head, slow
        L, R = self.sortList(L), self.sortList(R)
        return self.mergeTwoLists(L, R)

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


head = ListNode(10, ListNode(-1, ListNode(24, ListNode(13, ListNode(111)))))

inst = Solution()
head = inst.sortList(head)

while head:
    print(head.val, end=' ')
    head = head.next
print()
