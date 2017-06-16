from unittest import TestCase

from nose_parameterized import parameterized

from binary_tree_to_linked_list_using_inorder_traversal import Solution
from utils_linked_list import compare_linked_lists, get_head_linked_list
from utils_tree import construct_tree


class TestBinaryTreeToLinkedListUsingInorderTraversal(TestCase):
    @parameterized.expand([
        [
            {
                'root': construct_tree([
                    [4], [2, 6], [1, 3, 5, 7],
                ]),
            },
            get_head_linked_list([1, 2, 3, 4, 5, 6, 7]),
        ],
        [
            {
                'root': construct_tree([
                    [80], [70, 90], [None, 75, 85], [72, 76, None, 88],
                ]),
            },
            get_head_linked_list([70, 72, 75, 76, 80, 85, 88, 90]),
        ],
    ])
    def test_problem_to_solve(self, kwargs, expected_head):
        # Setup
        sol = Solution()

        # Exercise
        head = sol.tree_to_linked_list(**kwargs)

        # Verify
        self.assertTrue(compare_linked_lists(head, expected_head))
