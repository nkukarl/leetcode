from unittest import TestCase

from nose_parameterized import parameterized

from longest_palindrome import Solution


class TestLongestPalindrome(TestCase):
    @parameterized.expand([
        [
            {
                's': 'abccccdd',
            },
            7,
        ],
    ])
    def test_longest_palindrome(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.longest_palindrome(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
