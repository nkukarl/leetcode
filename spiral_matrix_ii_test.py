from unittest import TestCase

from nose_parameterized import parameterized

from spiral_matrix_ii import Solution


class TestSpiralMatrixII(TestCase):
    @parameterized.expand([
        [
            {
                'n': -1,
            },
            [],
        ],
        [
            {
                'n': 0,
            },
            [],
        ],
        [
            {
                'n': 1,
            },
            [[1]],
        ],
        [
            {
                'n': 4,
            },
            [
                [1, 2, 3, 4],
                [12, 13, 14, 5],
                [11, 16, 15, 6],
                [10, 9, 8, 7],
            ],
        ],
        [
            {
                'n': 5,
            },
            [
                [1, 2, 3, 4, 5],
                [16, 17, 18, 19, 6],
                [15, 24, 25, 20, 7],
                [14, 23, 22, 21, 8],
                [13, 12, 11, 10, 9],
            ],
        ],
    ])
    def test_generate_matrix(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.generate_matrix(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
