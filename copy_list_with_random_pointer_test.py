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
        random_linked_list_raw = random.sample(list(range(9)), 9)
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

    def test_copy_random_list_duplicated_labels(self):
        # Setup
        sol = Solution()
        random_linked_list_raw = [random.randint(1, 3) for _ in range(9)]
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
        labels1, randoms1 = self.summarise_random_linked_list(head1)
        labels2, randoms2 = self.summarise_random_linked_list(head2)
        return labels1 == labels2 and randoms1 == randoms2

    def summarise_random_linked_list(self, head):
        nodes = []
        labels = []
        randoms = []
        node = head
        while node is not None:
            labels.append(node.label)
            nodes.append(node)
            node = node.next
        for node in nodes:
            randoms.append(self.get_index(node.random, nodes))
        return labels, randoms

    def get_index(self, node_, nodes):
        for i, node in enumerate(nodes):
            if node_ == node:
                return i
        return None
