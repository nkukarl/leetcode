from utils_linked_list import ListNode


class Solution(object):
    def merge_two_lists(self, l1, l2):
        if l1 is None or l2 is None:
            return l1 or l2
        dummy = ListNode(0)
        node = dummy
        node1, node2 = l1, l2
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        if node1 is not None:
            node.next = node1
        else:
            node.next = node2
        return dummy.next
