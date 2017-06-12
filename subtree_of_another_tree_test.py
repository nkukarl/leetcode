from unittest import TestCase

from subtree_of_another_tree import Solution
from utils_tree import construct_tree


class TestSubtreeOfAnotherTree(TestCase):
    def test_is_subtree(self):
        # Setup
        sol = Solution()

        s_serialized_data = [[4], [2, 6], [1, 3, 5, 7]]
        s = construct_tree(s_serialized_data)

        t_serialized_data = [[2], [1, 3]]
        t = construct_tree(t_serialized_data)

        # Exercise
        ans = sol.is_subtree(s, t)

        # Verify
        self.assertTrue(ans)
