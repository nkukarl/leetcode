from unittest import TestCase

from nose_parameterized import parameterized

from utils_tree import get_root_tree
from validate_binary_search_tree import Solution


class TestValidateBinarySearchTree(TestCase):
    @parameterized.expand([
        [
            [1, 2, 3, 4, 5, 6, 7],
            True,
        ],
        [
            [1, 2, 3, 6, 5, 4, 7],
            False,
        ],
        [
            [1, 2, 3, 4, 3, 6, 7],
            False,
        ],
    ])
    def test_is_valid_bst(self, tree_raw, expected_ans):
        # Setup
        sol = Solution()
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.is_valid_bst(root)

        # Verify
        self.assertEqual(ans, expected_ans)
