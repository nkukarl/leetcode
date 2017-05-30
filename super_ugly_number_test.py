from unittest import TestCase

from nose_parameterized import parameterized

from super_ugly_number import Solution


class TestSuperUglyNumber(TestCase):
    @parameterized.expand([
        [
            {
                'n': 12,
                'primes': [2, 7, 13, 19],
            },
            32,
        ],
        [
            {
                'n': 100,
                'primes': [5, 11, 19, 23],
            },
            207575,
        ],
    ])
    def test_nth_super_ugly_number(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.nth_super_ugly_number(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
