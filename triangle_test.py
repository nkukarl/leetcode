from unittest import TestCase

from nose_parameterized import parameterized

from triangle import Solution


class TestTriangle(TestCase):
    @parameterized.expand([
        [
            {
                'triangle': [
                    [2],
                    [3, 4],
                    [6, 5, 7],
                    [4, 1, 8, 3],
                ],
            },
            11,
        ],
    ])
    def test_minimum_total(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.minimum_total(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
