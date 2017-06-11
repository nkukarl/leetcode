from unittest import TestCase

from nose_parameterized import parameterized

from binary_tree_tilt import Solution
from utils_tree import construct_tree


class TestBinaryTreeTilt(TestCase):
    @parameterized.expand([
        [
            [
                [2], [1, 3],
            ],
            2,
        ],
        [
            [
                [1], [2], [3, 4], [5, None, 6, 7], [None, 9],
            ],
            60,
        ]
    ])
    def test_find_tilt(self, serialized_data, expected_ans):
        # Setup
        sol = Solution()
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.find_tilt(root)

        # Verify
        self.assertEqual(ans, expected_ans)
