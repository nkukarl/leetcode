from unittest import TestCase

from nose_parameterized import parameterized

from perfect_number import Solution


class TestPerfectNumber(TestCase):
    @parameterized.expand([
        [
            {
                'num': 28,
            },
            True,
        ],
        [
            {
                'num': 6,
            },
            True,
        ],
        [
            {
                'num': 64,
            },
            False,
        ],
    ])
    def test_check_perfect_number(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.check_perfect_number(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
