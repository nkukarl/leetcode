from unittest import TestCase

from nose_parameterized import parameterized

from valid_perfect_square import Solution


class TestValidPerfectSquare(TestCase):
    @parameterized.expand([
        [
            1,
        ],
        [
            15,
        ],
        [
            16,
        ],
        [
            10001,
        ],
    ])
    def test_is_perfect_square(self, num):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.is_perfect_square(num)
        expected_ans = self.is_perfect_square(num)

        # Verify
        self.assertEqual(ans, expected_ans)

    def is_perfect_square(self, num):
        return int(num ** 0.5) ** 2 == num

    @parameterized.expand([
        [
            0,
        ],
        [
            1,
        ],
        [
            3,
        ],
        [
            13,
        ],
    ])
    def test_get_sqrt_approximate(self, num):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.get_sqrt_int(num)
        expected_ans = int(num ** 0.5)

        # Verify
        self.assertEqual(ans, expected_ans)
