from unittest import TestCase

from nose_parameterized import parameterized

from battleships_in_a_board import Solution


class TestBattleshipsInABoard(TestCase):
    @parameterized.expand([
        [
            {
                'board': [
                    'XX..X',
                    '....X',
                    '..X..',
                    '..X..',
                    'XX.XX',
                ],
            },
            5,
        ],
    ])
    def test_count_battleships(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.count_battleships(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
