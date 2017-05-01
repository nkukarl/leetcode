from unittest import TestCase

from nose_parameterized import parameterized

from count_numbers_with_unique_digits import Solution


class TestCountNumbersWithUniqueDigits(TestCase):
    @parameterized.expand([
        [
            2,
        ],
        [
            4,
        ],
        [
            6,
        ]
    ])
    def test_count_numbers_with_unique_digits(self, n):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.count_numbers_with_unique_digits(n)

        # Verify
        expected_ans = self.count_numbers_with_unique_digits(n)
        self.assertEqual(ans, expected_ans)

    def count_numbers_with_unique_digits(self, n):
        count = 0
        for i in range(10 ** n):
            digits = list(str(i))
            if len(digits) == len(set(digits)):
                count += 1
        return count
