from unittest import TestCase

from nose_parameterized import parameterized

from jump_game import Solution


class TestJumpGame(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [2, 3, 1, 1, 4],
            },
            True,
        ],
        [
            {
                'nums': [3, 2, 1, 0, 4],
            },
            False,
        ],
    ])
    def test_can_jump(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.can_jump(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
