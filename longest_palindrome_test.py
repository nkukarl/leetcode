from unittest import TestCase

from nose_parameterized import parameterized

from longest_palindrome import Solution


class TestLongestPalindrome(TestCase):
    @parameterized.expand([
        [
            {
                's': 'abccccdd',
            },
        ],
    ])
    def test_longest_palindrome(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.longest_palindrome(**kwargs)

        # Verify
        expected_ans = self.longest_palindrome(**kwargs)
        self.assertEqual(ans, expected_ans)

    def longest_palindrome(self, s):
        summary = {}
        for char in s:
            summary[char] = summary.get(char, 0) + 1

        flag = False
        ans = 0
        for char in summary:
            if summary[char] % 2 != 0:
                if not flag:
                    ans += summary[char]
                    flag = True
                else:
                    ans += summary[char] - 1
            else:
                ans += summary[char]
        return ans
