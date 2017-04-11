class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        slow = head
        fast = slow
        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
            if fast:
                slow.next = fast
                slow = slow.next
            else:
                slow.next = None
                return head


head = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(3,
                                                                            ListNode(
                                                                                3,
                                                                                ListNode(
                                                                                    4,
                                                                                    ListNode(
                                                                                        4,
                                                                                        ListNode(
                                                                                            5,
                                                                                            ListNode(
                                                                                                6,
                                                                                                ListNode(
                                                                                                    7))))))))))))

inst = Solution()
head = inst.deleteDuplicates(head)

while head:
    print(head.val, end=' ')
    head = head.next
print()
