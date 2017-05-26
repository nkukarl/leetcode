from unittest import TestCase

from nose_parameterized import parameterized

from search_a_2d_matrix_ii import Solution


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
                'matrix': [[5]],
                'target': 5,
            },
            True,
        ],
        [
            {
                'matrix': [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                'target': 20,
            },
            False,
        ],
        [
            {
                'matrix': [
                    [1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30],
                ],
                'target': 9,
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
