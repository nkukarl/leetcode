from unittest import TestCase

from nose_parameterized import parameterized

from surrounded_regions import Solution


class TestSurroundedRegions(TestCase):
    @parameterized.expand([
        [
            [
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'O', 'X'],
                ['X', 'X', 'O', 'X'],
                ['X', 'O', 'X', 'X'],
            ],
            [
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X'],
                ['X', 'O', 'X', 'X'],
            ],
        ],
    ])
    def test_solve(self, board, expected_board):
        # Setup
        sol = Solution()

        # Exercise
        sol.solve(board)

        # Verify
        self.assertEqual(board, expected_board)
