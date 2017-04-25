from unittest import TestCase

from min_stack import MinStack


class TestMinStack(TestCase):
    def test_min_stack(self):
        # Setup
        min_stack = MinStack()

        # Exercise and Verify
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-1)
        self.assertEqual(min_stack.get_min(), -2)
        self.assertEqual(min_stack.top(), -1)
        self.assertEqual(min_stack.pop(), -1)
        self.assertEqual(min_stack.get_min(), -2)
