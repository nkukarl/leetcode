class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(-2 ** 31)
        tail = dummy
        node = head
        while node:
            next = node.next
            node.next = None
            if node.val >= tail.val:
                tail.next = node
                tail = node
            else:
                self.insertion(dummy, node)
            node = next
        return dummy.next

    def insertion(self, head, node):
        cur = head
        prev = None
        while node.val > cur.val:
            prev = cur
            cur = cur.next
        prev.next = node
        node.next = cur


head = ListNode(10, ListNode(-1, ListNode(24, ListNode(13, ListNode(111)))))

inst = Solution()
head = inst.insertionSortList(head)

while head:
    print(head.val, end=' ')
    head = head.next
print()
