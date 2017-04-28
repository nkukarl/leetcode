import random
from unittest import TestCase

from nose_parameterized import parameterized

from find_mode_in_binary_search_tree import Solution
from utils_tree import get_root_tree


class TestFindModeInBST(TestCase):
    @parameterized.expand([
        [
            [],
            [],
        ],
        [
            [1] * 3,
            [1]
        ],
        [
            [1] * 3 + [2] * 2,
            [1]
        ],
        [
            [1] * 5 + [2] * 5 + [3] * 4,
            [1, 2],
        ],
    ])
    def test_find_mode(self, tree_raw, expected_ans):
        # Setup
        sol = Solution()
        random.shuffle(tree_raw)
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.find_mode(root)

        # Verify
        self.assertEqual(ans, expected_ans)
