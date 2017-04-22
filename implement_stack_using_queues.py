class MyStack(object):
    def __init__(self):
        """

        Initialize data structure here.

        """
        self.queue_a = []
        self.queue_b = []

    def push(self, x):
        """

        Push element x onto stack.

        """
        self.queue_a.append(x)

    def pop(self):
        """

        Removes the element on top of the stack and returns that element.

        """
        while len(self.queue_a) > 1:
            self.queue_b.append(self.queue_a.pop(0))
        res = self.queue_a.pop()
        self.queue_a, self.queue_b = self.queue_b, self.queue_a
        return res

    def top(self):
        """

        Get the top element.

        """
        val = None
        while len(self.queue_a) > 0:
            val = self.queue_a.pop(0)
            self.queue_b.append(val)
        self.queue_a, self.queue_b = self.queue_b, self.queue_a
        return val

    def empty(self):
        """

        Returns whether the stack is empty.

        """
        return 0 == len(self.queue_a)
