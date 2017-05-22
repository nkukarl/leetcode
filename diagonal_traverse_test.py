from unittest import TestCase

from nose_parameterized import parameterized

from diagonal_traverse import Solution


class TestDiagonalTraverse(TestCase):
    @parameterized.expand([
        [
            {
                'matrix': [
                    [1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                ],
            },
            [1, 2, 6, 7, 3, 4, 8, 9, 5, 10],
        ],
    ])
    def test_find_diagonal_order(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_diagonal_order(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
