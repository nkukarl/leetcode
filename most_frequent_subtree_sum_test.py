from unittest import TestCase

from nose_parameterized import parameterized

from most_frequent_subtree_sum import Solution
from utils_tree import construct_tree


class TestFindFrequentTreeSum(TestCase):
    @parameterized.expand([
        [
            [[5], [2, -3]],
            [2, -3, 4],
        ],
        [
            [[5], [2, -5]],
            [2],
        ],
    ])
    def test_find_frequent_tree_sum(self, serialized_data, expected_ans):
        # Setup
        sol = Solution()
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.find_frequent_tree_sum(root)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
