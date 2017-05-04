import random
from unittest import TestCase

from elimination_game import Solution


class TestEliminationGame(TestCase):
    def test_last_remaining(self):
        # Setup
        sol = Solution()
        n = random.randint(1, 100000000)

        # Exercise
        ans = sol.last_remaining(n)

        # Verify
        expected_ans = self.last_remaining(n)
        self.assertEqual(ans, expected_ans)

    def last_remaining(self, n):
        nums = range(1, n + 1)
        while len(nums) > 1:
            nums = nums[1::2][::-1]
        return nums[0]
