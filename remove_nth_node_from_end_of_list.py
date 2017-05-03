from utils_linked_list import ListNode


class Solution(object):
    def remove_nth_from_end(self, head, n):
        frontier = head
        while n > 0:
            frontier = frontier.next
            n -= 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        node = head
        while frontier is not None:
            frontier = frontier.next
            prev = node
            node = node.next
        prev.next = node.next
        return dummy.next
