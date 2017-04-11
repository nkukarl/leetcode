class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        L1 = self.mergeKLists(lists[:len(lists) // 2])
        L2 = self.mergeKLists(lists[len(lists) // 2:])
        return self.mergeTwoLists(L1, L2)

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


lists = [ListNode(1, ListNode(3, ListNode(5, ListNode(7)))),
         ListNode(2, ListNode(3, ListNode(6, ListNode(9)))), None,
         ListNode(3, ListNode(8)), ListNode(10, ListNode(15)),
         ListNode(9, ListNode(11, ListNode(12)))]

inst = Solution()
head = inst.mergeKLists(lists)

while head:
    print(head.val, end=' ')
    head = head.next
print()
