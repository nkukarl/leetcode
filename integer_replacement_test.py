from unittest import TestCase

from nose_parameterized import parameterized

from integer_replacement import Solution


class TestIntegerReplacement(TestCase):
    @parameterized.expand([
        [
            {
                'n': 7,
            },
            4,
        ],
        [
            {
                'n': 8,
            },
            3,
        ],
    ])
    def test_integer_replacement(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.integer_replacement(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
