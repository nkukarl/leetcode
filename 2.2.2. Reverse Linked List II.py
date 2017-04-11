class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, m, n):
        if m == n:
            return
        dummy = ListNode(0, head)
        counter = 0
        node = dummy
        while counter < m - 1:
            node = node.next
            counter += 1
        mark1 = node
        head = mark1.next

        node = head
        counter = 0
        while counter < n - m:
            node = node.next
            counter += 1
        mark2 = node.next
        node.next = None

        HEAD, TAIL = self.reverse(head)

        mark1.next = HEAD
        TAIL.next = mark2

        return dummy.next

    def reverse(self, head):
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev, head


head = ListNode(1,
                ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
m, n = 2, 3

inst = Solution()
head = inst.reverseBetween(head, m, n)

while head:
    print(head.val, end=' ')
    head = head.next
print()
