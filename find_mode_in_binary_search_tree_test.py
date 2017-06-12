import random
from unittest import TestCase

from nose_parameterized import parameterized

from find_mode_in_binary_search_tree import Solution
from utils_tree import construct_tree


class TestFindModeInBST(TestCase):
    @parameterized.expand([
        [
            construct_tree([]),
            [],
        ],
        [
            construct_tree([[1], [1, 1]]),
            [1],
        ],
        [
            construct_tree([[3], [3, 3], [2, None, 2]]),
            [3],
        ],
        [
            construct_tree(
                [[3], [3, 3], [2, 1, 2, 1], [2, 1, None, None, 2, 1]]
            ),
            [1, 2],
        ],
    ])
    def test_find_mode(self, root, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_mode(root)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
