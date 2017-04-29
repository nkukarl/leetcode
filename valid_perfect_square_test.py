import random
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
        expected_ans = int(num ** 0.5) ** 2 == num

        # Verify
        self.assertEqual(ans, expected_ans)

    def test_get_sqrt_approximate(self):
        # Setup
        sol = Solution()
        num = random.randint(1, 100000)

        # Exercise
        ans = sol.get_sqrt_approximate(num)
        expected_ans = num ** 0.5

        # Verify
        self.assertEqual(ans, int(expected_ans))
