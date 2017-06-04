from unittest import TestCase

from largest_palindrome_product import Solution


class TestLargestPalindromeProduct(TestCase):
    def test_largest_palindrome(self):
        # Setup
        sol = Solution()
        MAP = {
            1: 9,
            2: 987,
            3: 123,
            4: 597,
            5: 677,
            6: 1218,
            7: 877,
            8: 475,
        }

        # Exercise and Verify
        for n in range(1, 4):
            ans = sol.largest_palindrome(n)
            expected_ans = MAP[n]
            self.assertEqual(ans, expected_ans)
