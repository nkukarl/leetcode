class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head
        prev = None
        counter = 0
        while counter < n:
            fast = fast.next
            counter += 1
        if not fast:
            return head.next
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,
                                                                            ListNode(
                                                                                7)))))))

inst = Solution()
head = inst.removeNthFromEnd(head, 7)

while head:
    print(head.val, end=' ')
    head = head.next
print()
