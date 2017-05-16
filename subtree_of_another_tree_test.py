from unittest import TestCase

from subtree_of_another_tree import Solution
from utils_tree import get_root_tree


class TestSubtreeOfAnotherTree(TestCase):
    def test_is_subtree(self):
        # Setup
        sol = Solution()
        s_raw = [1, 2, 3, 4, 5, 6, 7]
        t_raw = [1, 2, 3]
        s, t = get_root_tree(s_raw), get_root_tree(t_raw)

        # Exercise
        ans = sol.is_subtree(s, t)

        # Verify
        self.assertTrue(ans)
