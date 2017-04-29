import random
from unittest import TestCase

from copy_list_with_random_pointer import RandomListNode, Solution


class TestCopyListWithRandomPointer(TestCase):
    def test_copy_random_list(self):
        # Setup
        sol = Solution()

        # # # # # # # # # # # # # # # # #
        #                               #
        #    . . . . . . . . . . . .    #
        #    .         . .         .    #
        #    .         . .         .    #
        #    v         . v         .    #
        #   [1]------->[2]------->[3]   #
        #    .                     ^    #
        #    .                     .    #
        #    .                     .    #
        #    . . . . . . . . . . . .    #
        #                               #
        # # # # # # # # # # # # # # # # #

        random_linked_list_raw = [1, 2, 3]
        head = self.get_head_random_linked_list(random_linked_list_raw)
        first, second, third = head, head.next, head.next.next
        first.random = third
        second.random = first
        third.random = second
        # Exercise
        head_copied = sol.copy_random_list(head)

        # Verify
        self.assertTrue(self.compare_random_linked_lists(head, head_copied))

    def test_copy_random_list_dynamically_generated(self):
        # Setup
        sol = Solution()
        random_linked_list_raw = random.sample(list(range(9)), 5)
        head = self.get_head_random_linked_list(random_linked_list_raw)
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next
        for node in nodes:
            node.random = random.choice(nodes)
        # Exercise
        head_copied = sol.copy_random_list(head)

        # Verify
        self.assertTrue(self.compare_random_linked_lists(head, head_copied))

    def get_head_random_linked_list(self, random_linked_list_raw):
        dummy = RandomListNode(0)
        node = dummy
        for label in random_linked_list_raw:
            node.next = RandomListNode(label)
            node = node.next
        return dummy.next

    def compare_random_linked_lists(self, head1, head2):
        if head1 is None and head2 is None:
            return True
        node1, node2 = head1, head2
        while node1 is not None and node2 is not None:
            if node1 == node2:  # Must be a copy
                return False
            if node1.label != node2.label:
                return False
            # Actually this comparison is not sufficient,
            # but the test cases would avoid using lists
            # of nodes with the same label.
            if node1.random.label != node2.random.label:
                return False
            node1 = node1.next
            node2 = node2.next
        if node1 is not None or node2 is not None:
            return False
        return True
