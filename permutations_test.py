from unittest import TestCase

from permutations import Solution


class TestPermutations(TestCase):
    def test_permute(self):
        # Setup
        sol = Solution()
        nums = [1, 2, 3]

        # Exercise
        ans = sol.permute(nums)
        expected_ans = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))

    def test_permute_unique(self):
        # Setup
        sol = Solution()
        nums = [1, 1, 2, 3]
        nums = [3,3,0,0,2,3,2]

        # Exercise
        ans = sol.permute_unique(nums)
        expected_ans = [
            [1, 1, 2, 3],
            [1, 1, 3, 2],
            [1, 2, 1, 3],
            [1, 2, 3, 1],
            [1, 3, 1, 2],
            [1, 3, 2, 1],
            [2, 1, 1, 3],
            [2, 1, 3, 1],
            [2, 3, 1, 1],
            [3, 1, 1, 2],
            [3, 1, 2, 1],
            [3, 2, 1, 1],
        ]

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
