from unittest import TestCase

from nose_parameterized import parameterized

from pascal_triangle import Solution


class TestPascalTriangle(TestCase):
    @parameterized.expand([
        [
            {
                'num_rows': 0,
            },
            [],
        ],
        [
            {
                'num_rows': 1,
            },
            [[1]],
        ],
        [
            {
                'num_rows': 2,
            },
            [[1], [1, 1]],
        ],
        [
            {
                'num_rows': 5,
            },
            [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        ],
    ])
    def test_generate(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.generate(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)

    @parameterized.expand([
        [
            {
                'row_index': 0,
            },
            [1],
        ],
        [
            {
                'row_index': 1,
            },
            [1, 1],
        ],
        [
            {
                'row_index': 2,
            },
            [1, 2, 1],
        ],
        [
            {
                'row_index': 5,
            },
            [1, 5, 10, 10, 5, 1],
        ],
    ])
    def test_get_row(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.get_row(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
