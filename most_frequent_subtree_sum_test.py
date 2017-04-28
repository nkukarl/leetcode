from unittest import TestCase

from nose_parameterized import parameterized

from most_frequent_subtree_sum import Solution
from utils_tree import get_root_tree


class TestFindFrequentTreeSum(TestCase):
    @parameterized.expand([
        [
            [2, 5, -3],
            [2, -3, 4],
        ],
        [
            [2, 5, -5],
            [2],
        ],
        [
            [1, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 2, 1],
            [2]
        ]
    ])
    def test_find_frequent_tree_sum(self, tree_raw, expected_ans):
        # Setup
        sol = Solution()
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.find_frequent_tree_sum(root)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
