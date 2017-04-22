from unittest import TestCase

from implement_stack_using_queues import MyStack


class TestMyStack(TestCase):
    def test_my_stack(self):
        # Setup
        stack = MyStack()

        # Exercise and Verify
        self.assertEqual(stack.empty(), True)
        stack.push(3)
        self.assertEqual(stack.empty(), False)
        stack.push(5)
        stack.push(6)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.top(), 5)
        self.assertEqual(stack.top(), 5)
