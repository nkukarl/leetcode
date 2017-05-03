class Solution(object):
    def get_intersection_node(self, head_1, head_2):
        length_1, length_2 = self.get_length(head_1), self.get_length(head_2)
        if length_1 < length_2:
            head_1, head_2 = head_2, head_1
        node_1, node_2 = head_1, head_2
        diff = abs(length_1 - length_2)
        while diff:
            node_1 = node_1.next
            diff -= 1
        while node_1 and node_2:
            if node_1 == node_2:
                return node_1
            node_1 = node_1.next
            node_2 = node_2.next
        return None

    def get_length(self, head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length
