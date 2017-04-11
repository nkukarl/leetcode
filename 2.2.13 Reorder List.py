class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None
            R = self.reverse(slow)
            L = head
            dummy = ListNode(0)
            node = dummy
            l, r = L, R
            while l and r:
                node.next = l
                node = node.next
                l = l.next
                node.next = r
                node = node.next
                r = r.next
            if l:
                node.next = l
            else:
                node.next = r
        return head

    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,
                                                                            ListNode(
                                                                                6,
                                                                                ListNode(
                                                                                    7))))))))
head = None
head = ListNode(1)

inst = Solution()
head = inst.reorderList(head)

while head:
    print(head.val, end=' ')
    head = head.next
print()
