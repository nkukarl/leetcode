from unittest import TestCase

from symmetric_tree import Solution
from utils_tree import construct_tree


class TestSymmetricTree(TestCase):
    def test_is_symmetric(self):
        # Setup
        sol = Solution()
        serialized_data = [[1], [2, 2], [3, 4, 4, 3]]
        root = construct_tree(serialized_data)

        # Exercise
        ans = sol.is_symmetric(root)

        # Verify
        self.assertTrue(ans)
