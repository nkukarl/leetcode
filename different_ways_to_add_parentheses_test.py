from unittest import TestCase

from nose_parameterized import parameterized

from different_ways_to_add_parentheses import Solution


class TestDifferentWaysToAddParentheses(TestCase):
    @parameterized.expand([
        [
            {
                's': '2-1-1',
            },
            [0, 2],
        ],
        [
            {
                's': '2*3-4*5',
            },
            [-34, -14, -10, -10, 10],
        ],
    ])
    def test_different_ways_to_compute(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.different_ways_to_compute(**kwargs)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
