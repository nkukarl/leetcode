from unittest import TestCase

from subsets import Solution


class TestSubsets(TestCase):
    def test_subsets(self):
        # Setup
        sol = Solution()
        nums = [1, 2, 3]

        # Exercise
        ans = sol.subsets(nums)
        expected_ans = [
            [],
            [1], [2], [3],
            [1, 2], [1, 3], [2, 3],
            [1, 2, 3]
        ]

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
