import random
from unittest import TestCase

from add_two_numbers import ListNode, Solution


class TestAddTwoNumbers(TestCase):
    def number_to_list(self, number):
        numbers = list(map(int, str(number)[::-1]))
        head = ListNode(numbers[0])
        node = head
        for n in numbers[1:]:
            node.next = ListNode(n)
            node = node.next
        return head

    def list_to_number(self, list):
        node = list
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return int(''.join(map(str, result[::-1])))

    def test_add_two_numbers(self):
        # Setup
        sol = Solution()
        number1 = random.randint(1, 1000)
        number2 = random.randint(1, 1000)
        l1 = self.number_to_list(number1)
        l2 = self.number_to_list(number2)

        # Exercise
        ans = sol.add_two_numbers(l1, l2)

        # Verify
        ans = self.list_to_number(ans)
        expected_ans = number1 + number2
        self.assertEqual(ans, expected_ans)
