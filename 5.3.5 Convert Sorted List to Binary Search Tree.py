class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def sortedListBST(self, head):
        n = self.getLength(head)
        return self.helper(head, n)

    def helper(self, head, n):
        if n == 0:
            return None
        if n == 1:
            return TreeNode(head.val)
        counter = 0
        cur = head
        prev = None
        while counter < n // 2:
            prev = cur
            cur = cur.next
            counter += 1
        prev.next = None
        leftHead = head
        rightHead = cur.next
        cur.next = None
        root = TreeNode(cur.val)
        root.left = self.helper(leftHead, counter)
        root.right = self.helper(rightHead, n - counter - 1)
        return root

    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,
                                                                            ListNode(
                                                                                7)))))))

inst = Solution()
root = inst.sortedListBST(head)
