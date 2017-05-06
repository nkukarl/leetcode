from unittest import TestCase

from nose_parameterized import parameterized

from palindrome_number import Solution


class TestPalindromeNumber(TestCase):
    @parameterized.expand([
        [
            {
                'n': 1010110101,
            },
            True,
        ],
        [
            {
                'n': 1000021,
            },
            False,
        ],
    ])
    def test_palindrome_number(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.is_palindrome(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
