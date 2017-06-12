from unittest import TestCase

from diameter_of_binary_tree import Solution
from utils_tree import construct_tree


class TestDiameterOfBinaryTree(TestCase):
    def test_diameter_of_binary_tree(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.diameter_of_binary_tree(root)

        # Verify
        expected_ans = 4
        self.assertEqual(ans, expected_ans)
