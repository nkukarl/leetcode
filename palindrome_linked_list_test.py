from unittest import TestCase

from palindrome_linked_list import Solution
from utils_linked_list import get_head_linked_list


class TestPalindromeLinkedList(TestCase):
    def test_is_palindrome(self):
        # Setup
        sol = Solution()
        # linked_list_raw = [1, 2, 3, 4, 3, 2, 1]
        # linked_list_raw = [1, 2, 3, 4, 4, 3, 2, 1]
        linked_list_raw = [1, 2, 3, 4, 4, 2, 1]
        head = get_head_linked_list(linked_list_raw)

        # Exercise
        ans = sol.is_palindrome(head)
        expected_ans = self.is_palindrome(linked_list_raw)

        # Verify
        self.assertEqual(ans, expected_ans)

    def is_palindrome(self, linked_list_raw):
        left, right = 0, len(linked_list_raw) - 1
        while left < right:
            if linked_list_raw[left] != linked_list_raw[right]:
                return False
            left += 1
            right -= 1
        return True
