class MyQueue(object):
    def __init__(self):
        """

        Initialize your data structure here.

        """
        self.stack_a = []
        self.stack_b = []

    def push(self, x):
        """

        Push element x to the back of queue.

        """
        self.stack_a.append(x)

    def pop(self):
        """

        Removes the element from in front of queue and returns that element.

        """
        if 0 == len(self.stack_b):
            while len(self.stack_a) > 0:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()

    def peek(self):
        """

        Get the front element.

        """
        if 0 == len(self.stack_b):
            while len(self.stack_a) > 0:
                self.stack_b.append(self.stack_a.pop())
        return self.stack_b[-1]

    def empty(self):
        """

        Returns whether the queue is empty.

        """
        return 0 == len(self.stack_a) and 0 == len(self.stack_b)
