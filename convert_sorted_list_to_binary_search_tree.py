from utils_linked_list import ListNode
from utils_tree import TreeNode


class Solution(object):
    def sorted_list_to_bst(self, head):
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        # Ensure a linked list with at least two nodes
        mid_node, left_list, right_list = self.split_linked_list(head)
        root = TreeNode(mid_node.val)
        root.left = self.sorted_list_to_bst(left_list)
        root.right = self.sorted_list_to_bst(right_list)
        return root

    def split_linked_list(self, head):
        """

        N.B. This method requires the linked list to have at least
        two nodes.

        Split a linked list into list_left, mid_node and list_right
        If the length of the original list is an even number,
        list_right is one node fewer than list_left.
        Otherwise, list_right and list_left are of equal length.

        Args:
            head (ListNode):

        Returns:
            list_left, mid_node, list_right

        """
        fast, slow = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # Split list_left
        prev.next = None

        list_left = head
        list_right = slow.next
        # Mark mid_node and split list_right
        mid_node = slow
        slow.next = None
        return mid_node, list_left, list_right
