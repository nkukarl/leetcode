from unittest import TestCase

from palindrome_number import Solution


class TestPalindromeNumber(TestCase):
    def test_palindrome_number(self):
        # Setup
        sol = Solution()
        n = 1010110101

        # Exercise
        ans = sol.is_palindrome(n)

        # Verify
        self.assertTrue(ans)
