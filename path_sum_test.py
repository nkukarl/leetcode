import random
from unittest import TestCase

from nose_parameterized import parameterized

from path_sum import Solution
from utils_tree import get_root_tree, construct_tree


class TestPathSum(TestCase):
    def test_has_path_sum(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)
        sum_ = random.choice([7, 9, 15, 17])

        # Exercise
        ans = sol.has_path_sum(root, sum_)

        # Verify
        self.assertTrue(ans)

    def test_full_path_sum(self):
        # Setup
        sol = Solution()
        tree_raw = [1, 2, 3, 4, 5, 6, 7]
        root = get_root_tree(tree_raw)
        sum_path_map = {
            7: [[4, 2, 1]],
            9: [[4, 2, 3]],
            15: [[4, 6, 5]],
            17: [[4, 6, 7]],
        }
        sum_ = random.choice(list(sum_path_map.keys()))

        # Exercise
        ans = sol.full_path_sum(root, sum_)
        expected_ans = sum_path_map[sum_]

        # Verify
        self.assertEqual(ans, expected_ans)

    @parameterized.expand([
        [
            [
                [10], [5, -3], [3, 2, None, 11], [3, -2, None, 1],
            ],
            8,
            3,
        ],
        [
            [
                [1], [1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1],
            ],
            2,
            11,
        ],
    ])
    def test_path_sum(self, serialized_data, sum_, expected_ans):
        # Setup
        sol = Solution()
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.path_sum(root, sum_)

        # Verify
        self.assertEqual(ans, expected_ans)