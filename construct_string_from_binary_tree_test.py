from unittest import TestCase

from nose_parameterized import parameterized

from construct_string_from_binary_tree import Solution
from utils_tree import construct_tree


class TestConstructStringFromBinaryTree(TestCase):
    @parameterized.expand([
        [
            [[1], [2, 3], [4]],
            '1(2(4))(3)',
        ],
        [
            [[1], [2, 3], [None, 4]],
            '1(2()(4))(3)',
        ],
        [
            [[1], [2, 3], [4, 5, 6, 7]],
            '1(2(4)(5))(3(6)(7))',
        ]
    ])
    def test_tree_to_str(self, tree_raw, expected_ans):
        # Setup
        sol = Solution()
        root = construct_tree(tree_raw)

        # Exercise
        ans = sol.tree_to_str(root)

        # Verify
        self.assertEqual(ans, expected_ans)
