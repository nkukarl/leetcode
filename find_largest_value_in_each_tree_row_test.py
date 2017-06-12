from unittest import TestCase

from nose_parameterized import parameterized

from find_largest_value_in_each_tree_row import Solution
from utils_tree import construct_tree


class TestFindLargestValueInEachTreeRow(TestCase):
    @parameterized.expand([
        [
            [[4], [2, 6], [1, 3, 5, 7]],
            [4, 6, 7],
        ],
        [
            [[4], [9, 6], [1, 3, 5]],
            [4, 9, 5],
        ],
    ])
    def test_largest_values(self, serialized_data, expected_ans):
        # Setup
        sol = Solution()
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.largest_values(root)

        # Verify
        self.assertEqual(ans, expected_ans)
