from unittest import TestCase

from nose_parameterized import parameterized

from jump_game_ii import Solution


class TestJumpGameII(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [0],
            },
            0,
        ],
        [
            {
                'nums': [2, 3, 1, 1, 4],
            },
            2,
        ],
        [
            {
                'nums': [2, 0, 1, 3, 4],
            },
            3,
        ],
        [
            {
                'nums': [1] * 100000,
            },
            99999,
        ],
    ])
    def test_jump(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.jump(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
