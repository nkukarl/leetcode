from unittest import TestCase

from nose_parameterized import parameterized

from super_pow import Solution


class TestSuperPow(TestCase):
    @parameterized.expand([
        [
            {
                'a': 29,
                'b': [
                    1, 3, 5, 7,
                ],
            },
        ],
        [
            {
                'a': 34,
                'b': [
                    3, 3,
                ],
            }
        ],
        [
            {
                'a': 4978626,
                'b': [
                    9, 6, 7, 6, 8, 3, 8, 9, 5, 6, 8, 2, 8, 7, 1, 8, 1, 9, 7, 0,
                    1, 5, 6, 8, 4, 0, 1, 8, 4, 2, 5, 9, 8, 4, 5, 9, 8, 5, 8, 5,
                    2, 8, 9, 0, 6, 2, 0, 9, 1, 8, 9, 4, 3, 2, 4, 6, 1, 2, 5, 8,
                ],
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
