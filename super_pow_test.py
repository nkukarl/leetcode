from unittest import TestCase

from nose_parameterized import parameterized

from super_pow import Solution


class TestSuperPow(TestCase):
    @parameterized.expand([
        [
            {
                'a': 29,
                'b': [1, 3, 5, 7],
            },
        ],
        [
            {
                'a': 34,
                'b': [3, 3],
            }
        ],
    ])
    def test_super_pow(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.super_pow(**kwargs)
        expected_ans = self.super_power(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)

    def super_power(self, a, b):
        if 1 == a:
            return 1
        n = int(''.join(map(str, b)))
        return a ** n % 1337
