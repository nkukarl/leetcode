from unittest import TestCase

from nose_parameterized import parameterized

from largest_palindrome_product import Solution


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

class TestLargestPalindromeProduct(TestCase):
    @parameterized.expand([
        [
            1,
        ],
        [
            2,
        ],
        [
            3,
        ],
        [
            4,
        ],
        [
            5,
        ],
        [
            6,
        ],
        [
            7,
        ],
        [
            8,
        ],
    ])
    def test_largest_palindrome(self, n):
        # Setup
        sol = Solution()

        # Exercise and Verify
        ans = sol.largest_palindrome(n)
        expected_ans = MAP[n]
        self.assertEqual(ans, expected_ans)
