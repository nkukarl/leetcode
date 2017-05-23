from unittest import TestCase

from nose_parameterized import parameterized

from find_min_path_in_maze import Solution


class TestFindMinPath(TestCase):
    @parameterized.expand([
        [
            {
                'maze': [
                    '01011111',
                    '00110011',
                    '10110110',
                    '11000111',
                ],
                'origin': [1, 2],
                'dest': [3, 7],
            },
            9,
        ],
        [
            {
                'maze': [
                    '11111111111111111111',
                    '11000000100111100011',
                    '10000111100011100001',
                    '10000000000000000001',
                    '11111111111111111111',
                ],
                'origin': [1, 1],
                'dest': [1, 18],
            },
            19,
        ],
        [
            {
                'maze': [
                    '1011110111',
                    '1010111011',
                    '1110110101',
                    '0000100001',
                    '1110111110',
                    '1011110100',
                    '1000000001',
                    '1011110111',
                    '1100001001',
                ],
                'origin': [0, 0],
                'dest': [3, 4],
            },
            11,
        ],
        [
            {
                'maze': [
                    '110000',
                    '010011',
                    '110001',
                    '101111',
                    '111000',
                ],
                'origin': [0, 0],
                'dest': [1, 4],
            },
            15,
        ],
        [
            {
                'maze': [
                    '01111',
                    '11101',
                    '00010',
                    '00101',
                    '11111',
                ],
                'origin': [0, 1],
                'dest': [2, 3],
            },
            -1,
        ],

    ])
    def test_find_min_path(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_min_path(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
