from unittest import TestCase

from climbing_stairs import Solution


class TestClimbingStairs(TestCase):
    def test_climbing_stairs(self):
        # Setup
        sol = Solution()
        n = 5

        # Exercise
        ans = sol.climbing_stairs(n)

        # Verify
        self.assertEqual(ans, 8)
