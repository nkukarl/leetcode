from unittest import TestCase

from unique_paths import Solution


class TestUniquePaths(TestCase):
    def test_unique_paths(self):
        # Setup
        sol = Solution()
        m, n = 3, 7

        # Exercise
        ans = sol.unique_paths(m, n)

        # Verify
        self.assertEqual(ans, 28)
