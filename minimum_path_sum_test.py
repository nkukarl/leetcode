from unittest import TestCase

from minimum_path_sum import Solution


class TestMinimumPathSum(TestCase):
    def test_min_path_sum(self):
        # Setup
        sol = Solution()
        grid = [
            [1, 2, 2, 1],
            [3, 3, 4, 2],
            [1, 4, 1, 2],
            [2, 2, 3, 3],
            [2, 1, 3, 2],
        ]

        # Exercise
        ans = sol.min_path_sum(grid)

        # Verify
        expected_ans = 15
        self.assertEqual(ans, expected_ans)
