from unittest import TestCase

from find_min_path_in_maze import Solution


class TestFindMinPath(TestCase):
    def test_find_min_path(self):
        # Setup
        sol = Solution()
        maze = [
            '11111111111111111111',
            '11000000100111100011',
            '10000111100011100001',
            '10000000000000000001',
            '11111111111111111111',
        ]
        xa, ya = 1, 1
        xb, yb = 1, 18

        # Exercise
        ans = sol.find_min_path(maze, xa, ya, xb, yb)
        pass

        # Verify
        # self.assertEqual(ans, expected_ans)
