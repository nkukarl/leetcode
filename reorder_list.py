from utils_linked_list import ListNode


class Solution(object):
    def reorder_list(self, head):
        # Handle simple scenarios where length of list is 0, 1 or 2
        if head is None or head.next is None or head.next.next is None:
            return head
        # Split list, mark the head of the second half as slow
        fast, slow = head, head
        prev = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None  # Split
        # Reverse the second half and mark its head as list_right
        list_left = head
        list_right = self._reverse_list(slow)
        # Create the reordered list
        node_left, node_right = list_left, list_right
        # The above split method would ensure length of list_right
        # is greater than or equal to list_left
        dummy = ListNode(0)
        node = dummy
        while node_left is not None:
            # Get node from list_left
            node.next = node_left
            node_left = node_left.next
            node = node.next
            # Get node from list_right
            node.next = node_right
            node_right = node_right.next
            node = node.next
        # If there is one more node in list_right
        if node_right is not None:
            node.next = node_right
        return dummy.next

    def _reverse_list(self, head):
        node = head
        prev = None
        while node is not None:
            next_ = node.next
            node.next = prev
            prev = node
            node = next_
        return prev
