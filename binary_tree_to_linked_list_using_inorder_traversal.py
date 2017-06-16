from utils_linked_list import ListNode


class Solution(object):
    def tree_to_linked_list(self, root):
        dummy = prev = ListNode(0)
        self.stack = []
        self.push_left(root)
        while self.stack:

            tree_node = self.stack.pop()
            self.push_left(tree_node.right)

            linked_list_node = ListNode(tree_node.val)
            prev.next = linked_list_node
            prev = prev.next
        return dummy.next


    def push_left(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left
