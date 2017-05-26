from unittest import TestCase

from nose_parameterized import parameterized

from spiral_matrix import Solution


class TestSpiralMatrix(TestCase):
    @parameterized.expand([
        [
            {
                'matrix': [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                ]
            },
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ],
        [
            {
                'matrix': [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16],
                ]
            },
            [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10],
        ],
        [
            {
                'matrix': [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                ]
            },
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ],
        [
            {
                'matrix': [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12],
                ]
            },
            [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8],
        ],
    ])
    def test_spiral_order(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.spiral_order(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
