from utils_linked_list import ListNode


class Solution(object):
    def add_two_numbers(self, head1, head2):
        stack1 = self.get_stack(head1)
        stack2 = self.get_stack(head2)
        stack = []
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0:
            val1 = stack1.pop() if len(stack1) > 0 else 0
            val2 = stack2.pop() if len(stack2) > 0 else 0
            res = val1 + val2 + carry
            val = res % 10
            carry = res // 10
            stack.append(val)
        if 1 == carry:
            stack.append(1)

        dummy = ListNode(0)
        node = dummy
        while len(stack) > 0:
            node.next = ListNode(stack.pop())
            node = node.next
        return dummy.next

    def get_stack(self, head):
        stack = []
        node = head
        while node is not None:
            stack.append(node.val)
            node = node.next
        return stack
