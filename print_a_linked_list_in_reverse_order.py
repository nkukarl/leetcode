class Solution(object):
    def print_in_reverse(self, head):
        """

        Print out a linked list in reverse order.

        Args:
            head (ListNode):

        """
        if head is not None:
            self.print_in_reverse(head.next)
            print(head.val, end=' ')
