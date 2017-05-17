from unittest import TestCase

from nose_parameterized import parameterized

from reshape_the_matrix import Solution


class TestReshapeTheMatrix(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [[1, 2, 3, 4], [5, 6, 7, 8]],
                'r': 4,
                'c': 2,
            },
            [[1, 2], [3, 4], [5, 6], [7, 8]],
        ],
        [
            {
                'nums': [[1, 2, 3], [4, 5, 6]],
                'r': 1,
                'c': 6,
            },
            [[1, 2, 3, 4, 5, 6]],
        ],
    ])
    def test_matrix_reshape(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.matrix_reshape(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
