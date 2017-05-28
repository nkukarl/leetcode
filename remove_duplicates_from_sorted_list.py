class Solution(object):
    def delete_duplicates(self, head):
        if head is None or head.next is None:
            return head
        cur = head
        cur_val = head.val
        node = head.next
        while node is not None:
            while node is not None and node.val == cur_val:
                node = node.next
            cur.next = node
            cur = node
            if node is not None:
                cur_val = node.val
        return head
