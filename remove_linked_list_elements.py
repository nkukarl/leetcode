class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def remove_elements(self, head, val):
        # Create a dummy node and let its next be head
        dummy = ListNode(val - 1)
        dummy.next = head

        node = dummy
        while node is not None:
            next_ = node.next
            while next_ is not None and next_.val == val:
                next_ = next_.next
                node.next = next_
            node = next_

        return dummy.next
