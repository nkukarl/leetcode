from unittest import TestCase

from nose_parameterized import parameterized

from island_perimeter import Solution


class TestIslandPerimeter(TestCase):
    @parameterized.expand([
        [
            [
                [0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0],
            ],
            16
        ],
    ])
    def test_island_perimeter(self, grid, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.island_perimeter(grid)

        # Verify
        self.assertEqual(ans, expected_ans)

    @parameterized.expand([
        [
            [0, 1, 0, 0],
            0
        ],
        [
            [0, 1, 1, 0],
            2
        ],
        [
            [1, 1, 1, 0, 0, 1, 1],
            6
        ],
    ])
    def test_get_overlapped(self, row, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.get_overlapped(row)

        # Verify
        self.assertEqual(ans, expected_ans)
