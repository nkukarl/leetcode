class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        dummy = ListNode(x - 1, head)
        prev = None
        slow = dummy
        while slow and slow.val < x:
            prev = slow
            slow = slow.next
        slow = prev
        fast = slow.next
        while fast:
            while fast and fast.val >= x:
                prev = fast
                fast = fast.next
            if fast:
                prev.next = fast.next
                tmp = slow.next
                slow.next = fast
                fast.next = tmp
                slow = slow.next
                fast = prev.next

        return dummy.next


head = ListNode(5,
                ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(6))))))

inst = Solution()
head = inst.partition(head, 4)

while head:
    print(head.val, end=' ')
    head = head.next
print()
