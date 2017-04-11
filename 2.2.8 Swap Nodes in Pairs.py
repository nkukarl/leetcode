class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):

        k = 2

        dummy = ListNode(0, head)
        prevT = dummy
        cur = head

        while cur:
            head = cur
            counter = 0
            while cur and counter < k - 1:
                cur = cur.next
                counter += 1
            if cur:
                next = cur.next
                cur.next = None
                H, T = self.reverse(head)
                prevT.next = H
                T.next = next
                prevT = T
                cur = next
            else:
                return dummy.next
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


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,
                                                                            ListNode(
                                                                                7,
                                                                                ListNode(
                                                                                    8,
                                                                                    ListNode(
                                                                                        9,
                                                                                        ListNode(
                                                                                            10))))))))))
# head = ListNode(0)
# head = None

inst = Solution()
head = inst.swapPairs(head)

while head:
    print(head.val, end=' ')
    head = head.next
print()
