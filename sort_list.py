from utils_linked_list import ListNode


class Solution(object):
    def sort_list(self, head):
        if head is None or head.next is None:
            return head
        left, right = self.split(head)
        left = self.sort_list(left)
        right = self.sort_list(right)
        return self.merge(left, right)

    def split(self, head):
        fast, slow = head, head
        prev = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        return head, slow

    def merge(self, head_1, head_2):
        dummy = ListNode(0)
        node = dummy
        while head_1 is not None and head_2 is not None:
            if head_1.val < head_2.val:
                node.next = head_1
                head_1 = head_1.next
            else:
                node.next = head_2
                head_2 = head_2.next
            node = node.next
        if head_1 is None:
            node.next = head_2
        else:
            node.next = head_1
        return dummy.next
