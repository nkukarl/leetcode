import random
from unittest import TestCase

from reorder_list import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list


class TestReorderList(TestCase):
    def test_reorder_list(self):
        # Setup
        sol = Solution()
        N = random.randint(0, 6)
        N = 5
        linked_list_raw = [n for n in range(N)]
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        head = sol.reorder_list(head)
        expected_head = self.get_expected_head(linked_list_raw)

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))

    def get_expected_head(self, original_linked_list_raw):
        linked_list_raw = []
        left, right = 0, len(original_linked_list_raw) - 1
        while left <= right:
            linked_list_raw.append(original_linked_list_raw[left])
            left += 1
            if left <= right:
                linked_list_raw.append(original_linked_list_raw[right])
                right -= 1
        return get_head_linked_list(linked_list_raw)
