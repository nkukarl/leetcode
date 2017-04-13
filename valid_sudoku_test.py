from unittest import TestCase
from valid_sudoku import Solution


class TestValidSudoku(TestCase):
    def test_is_valid_sudoku(self):
        # Setup
        sol = Solution()
        board = [
            '53..7....',
            '6..195...',
            '.98....6.',
            '8...6...3',
            '4..8.3..1',
            '7...2...6',
            '.6....28.',
            '...419..5',
            '....8..79',
        ]

        # Exercise
        ans = sol.is_valid_sudoku(board)

        # Verify
        self.assertTrue(ans)
