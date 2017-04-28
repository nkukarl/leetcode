from unittest import TestCase

from nose_parameterized import parameterized

from find_largest_value_in_each_tree_row import Solution
from utils_tree import get_root_tree


class TestFindLargestValueInEachTreeRow(TestCase):
    @parameterized.expand([
        [
            [1, 2, 3, 4, 5, 6, 7],
            [4, 6, 7],
        ],
        [
            [1, 9, 3, 4, 5, 6, None],
            [4, 9, 5],
        ],
    ])
    def test_largest_values(self, tree_raw, expected_ans):
        # Setup
        sol = Solution()
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.largest_values(root)

        # Verify
        self.assertEqual(ans, expected_ans)
