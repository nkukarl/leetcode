from unittest import TestCase

from nose_parameterized import parameterized

from search_a_2d_matrix import Solution


class TestSearchA2DMatrix(TestCase):
    @parameterized.expand([
        [
            {
                'matrix': [],
                'target': 5,
            },
            False,
        ],
        [
            {
                'matrix': [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                'target': 14,
            },
            False,
        ],
        [
            {
                'matrix': [
                    [1, 3, 5, 7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50],
                ],
                'target': 11,
            },
            True,
        ],
    ])
    def test_search_matrix(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.search_matrix(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
