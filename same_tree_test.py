from unittest import TestCase

from same_tree import Solution
from utils_tree import get_root_tree


class TestSameTree(TestCase):
    def test_is_same_tree(self):
        # Setup
        sol = Solution()
        root1 = get_root_tree([1, 2, 3, 4])
        root2 = get_root_tree([1, 2, 3, 4])

        # Exercise
        ans = sol.is_same_tree(root1, root2)

        # Verify
        self.assertTrue(ans)
