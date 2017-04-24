import random
from unittest import TestCase

from partition_list import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestPartitionList(TestCase):
    def test_partition(self):
        # Setup
        sol = Solution()
        linked_list_raw = [n for n in range(1, 6)] * 2
        random.shuffle(linked_list_raw)
        head = get_head_linked_list(linked_list_raw)
        x = random.randint(1, 5)

        # Exercise
        head = sol.partition(head, x)
        expected_head = get_head_linked_list(
            list(filter(lambda n: n < x, linked_list_raw)) +
            list(filter(lambda n: n >= x, linked_list_raw))
        )

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))
