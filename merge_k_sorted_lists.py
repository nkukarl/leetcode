from utils_linked_list import ListNode


class Solution(object):
    def merge_k_lists(self, linked_lists):
        self.MAX = 2 ** 31
        self.nodes = [head for head in linked_lists if head is not None]
        self.heapify()
        dummy = ListNode(0)
        node = dummy
        while len(self.nodes):
            node_ = self.pop_current_min()
            node.next = node_
            node = node.next
            if node_.next is not None:
                self.add_node(node_.next)
        return dummy.next

    def heapify(self):
        k = len(self.nodes) // 2 - 1
        while k >= 0:
            self.sift_down(k)
            k -= 1

    def pop_current_min(self):
        self.nodes[0], self.nodes[-1] = self.nodes[-1], self.nodes[0]
        node = self.nodes.pop()
        if len(self.nodes) > 0:
            self.sift_down(0)
        return node

    def add_node(self, node):
        self.nodes.append(node)
        self.sift_up(len(self.nodes) - 1)

    def sift_up(self, k):
        while (k - 1) // 2 >= 0:
            k_parent = (k - 1) // 2
            node_val = self.nodes[k].val
            node_parent_val = self.nodes[k_parent].val
            if node_val >= node_parent_val:
                break
            self.nodes[k], self.nodes[k_parent] = \
                self.nodes[k_parent], self.nodes[k]
            k = k_parent

    def sift_down(self, k):
        while True:
            node_val = self.nodes[k].val
            left, right = k * 2 + 1, k * 2 + 2
            node_left_val = \
                self.nodes[left].val if left < len(self.nodes) else self.MAX
            node_right_val = \
                self.nodes[right].val if right < len(self.nodes) else self.MAX
            if node_left_val > node_val < node_right_val:
                break
            if node_left_val < node_right_val:
                self.nodes[k], self.nodes[left] = \
                    self.nodes[left], self.nodes[k]
                k = left
            else:
                self.nodes[k], self.nodes[right] = \
                    self.nodes[right], self.nodes[k]
                k = right
