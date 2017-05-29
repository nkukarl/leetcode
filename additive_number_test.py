from unittest import TestCase

from nose_parameterized import parameterized

from additive_number import Solution


class TestAdditiveNumber(TestCase):
    @parameterized.expand([
        [
            {
                'num': '112358',
            },
            True,
        ],
        [
            {
                'num': '199100199',
            },
            True,
        ],
        [
            {
                'num': '1111',
            },
            False,
        ]
    ])
    def test_is_additive_number(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.is_additive_number(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
