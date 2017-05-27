from unittest import TestCase

from symmetric_tree import Solution
from utils_tree import get_root_tree


class TestSymmetricTree(TestCase):
    def test_is_symmetric(self):
        # Setup
        sol = Solution()
        tree_raw = [3, 2, 4, 1, 4, 2, 3]
        root = get_root_tree(tree_raw)

        # Exercise
        ans = sol.is_symmetric(root)

        # Verify
        self.assertTrue(ans)
