class Solution(object):
    def swap_pairs(self, head):
        if head is None or head.next is None:
            return head
        second = head.next
        next_ = self.swap_pairs(head.next.next)

        head.next = next_
        second.next = head
        return second
