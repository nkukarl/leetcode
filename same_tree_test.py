from unittest import TestCase

from same_tree import Solution
from utils_tree import construct_tree


class TestSameTree(TestCase):
    def test_is_same_tree(self):
        # Setup
        sol = Solution()
        serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        root1 = construct_tree(serialized_data)
        root2 = construct_tree(serialized_data)

        # Exercise
        ans = sol.is_same_tree(root1, root2)

        # Verify
        self.assertTrue(ans)
