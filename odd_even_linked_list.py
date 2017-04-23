class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def odd_even_list(self, head):
        # Handle simple scenarios: list length is 0, 1 or 2
        if head is None or head.next is None or head.next.next is None:
            return head
        # Mark the head of the even list
        head_even = head.next
        # Mark the looping odd element and even element
        odd, even = head, head.next
        # Mark the starting node
        node = head.next.next
        while node is not None:
            odd.next = node
            even.next = node.next
            odd = odd.next
            even = even.next
            # Mark the next node
            node = None if even is None else even.next
        # Link the end of the odd list to the head of the even list
        odd.next = head_even
        return head
