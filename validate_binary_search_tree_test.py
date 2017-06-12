from unittest import TestCase

from nose_parameterized import parameterized

from utils_tree import construct_tree
from validate_binary_search_tree import Solution


class TestValidateBinarySearchTree(TestCase):
    @parameterized.expand([
        [
            [[4], [2, 6], [1, 3, 5, 7]],
            True,
        ],
        [
            [[4], [2, 5], [1, 3, 6, 7]],
            False,
        ],
        [
            [[4], [2, 6], [7, 3, 5, 1]],
            False,
        ],
    ])
    def test_is_valid_bst(self, serialized_data, expected_ans):
        # Setup
        sol = Solution()
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.is_valid_bst(root)

        # Verify
        self.assertEqual(ans, expected_ans)
