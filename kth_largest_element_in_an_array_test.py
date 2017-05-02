import copy
import random
from unittest import TestCase

from kth_largest_element_in_an_array import Solution


class TestKthLargestElementInAnArray(TestCase):
    def test_find_kth_largest(self):
        # Setup
        sol = Solution()
        N = 100
        nums = [random.randint(1, 100) for _ in range(N)]
        random.shuffle(nums)

        # Exercise and Verify
        for k in range(1, N + 1):
            nums_ = copy.deepcopy(nums)
            ans = sol.find_kth_largest(nums_, k)
            expected_ans = sorted(nums, reverse=True)[k - 1]
            self.assertEqual(ans, expected_ans)

        # Exercise and Verify
        k = N + 1
        nums_ = copy.deepcopy(nums)
        with self.assertRaises(ValueError):
            sol.find_kth_largest(nums_, k)
