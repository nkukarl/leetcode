from utils_linked_list import ListNode


class Solution(object):
    def partition(self, head, x):
        if head is None or head.next is None:
            return head
        # Create two dummy heads
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less = less_head
        greater = greater_head
        node = head
        while node is not None:
            if node.val < x:
                less.next = node
                less = less.next
            else:
                greater.next = node
                greater = greater.next
            node = node.next
        less.next = greater_head.next
        # Mark the end of the greater list as None
        greater.next = None
        return less_head.next
