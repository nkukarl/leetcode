from unittest import TestCase

from unique_paths_ii import Solution


class TestUniquePathsII(TestCase):
    def test_unique_paths_with_obstacles(self):
        # Setup
        sol = Solution()
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]

        # Exercise
        ans = sol.unique_paths_with_obstacles(grid)

        # Verify
        self.assertEqual(ans, 2)
