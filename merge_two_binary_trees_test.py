from unittest import TestCase

from nose_parameterized import parameterized

from merge_two_binary_trees import Solution
from utils_tree import compare_trees, construct_tree


class TestMergeTwoBinaryTrees(TestCase):
    @parameterized.expand([
        [
            {
                't1': construct_tree([]),
                't2': construct_tree([
                    [1], [2],
                ]),
            },
            construct_tree([
                [1], [2],
            ]),
        ],
        [
            {
                't1': construct_tree([
                    [3], [1, 5], [None, 3, 5],
                ]),
                't2': construct_tree([
                    [1], [1, 1], [1, None, None, 7],
                ]),
            },
            construct_tree([
                [4], [2, 6], [1, 3, 5, 7],
            ]),
        ],
    ])
    def test_merge_trees(self, kwargs, expected_root):
        # Setup
        sol = Solution()

        # Exercise
        root = sol.merge_trees(**kwargs)

        # Verify
        self.assertTrue(compare_trees(root, expected_root))
