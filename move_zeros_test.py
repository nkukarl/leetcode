import random
from unittest import TestCase

from move_zeros import Solution


class TestMoveZeros(TestCase):
    def test_move_zeros(self):
        # Setup
        sol = Solution()
        nums = [0] * 10 + [i for i in range(1, 10)]
        random.shuffle(nums)
        expected_nums = self.move_zeros_as_a_copy(nums)

        # Exercise
        sol.move_zeros(nums)

        # Verify
        self.assertEqual(nums, expected_nums)

    def move_zeros_as_a_copy(self, nums):
        non_zeros, zeros = [], []
        for n in nums:
            if n != 0:
                non_zeros.append(n)
            else:
                zeros.append(n)
        return non_zeros + zeros
