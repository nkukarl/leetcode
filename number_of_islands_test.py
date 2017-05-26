from unittest import TestCase

from nose_parameterized import parameterized

from number_of_islands import Solution


class TestNumberOfIslands(TestCase):
    @parameterized.expand([
        [
            {
                'grid': [],
            },
            0,
        ],
        [
            {
                'grid': [['0']],
            },
            0,
        ],
        [
            {
                'grid': [['1']],
            },
            1,
        ],
        [
            {
                'grid': [
                    ['1', '1', '1', '1', '0'],
                    ['1', '1', '0', '1', '0'],
                    ['1', '1', '0', '0', '0'],
                    ['0', '0', '0', '0', '0'],
                ],
            },
            1,
        ],
        [
            {
                'grid': [
                    ['1', '1', '0', '0', '0'],
                    ['1', '1', '0', '0', '0'],
                    ['0', '0', '1', '0', '0'],
                    ['0', '0', '0', '1', '1'],
                ]
            },
            3,
        ],
    ])
    def test_num_islands(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.num_islands(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
