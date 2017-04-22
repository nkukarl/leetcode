from unittest import TestCase

from implement_queue_using_stacks import MyQueue


class TestMyQueue(TestCase):
    def test_my_queue(self):
        # Setup
        queue = MyQueue()

        # Exercise and Verify
        self.assertEqual(queue.empty(), True)
        queue.push(3)
        self.assertEqual(queue.empty(), False)
        queue.push(5)
        queue.push(6)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.peek(), 5)
        self.assertEqual(queue.peek(), 5)