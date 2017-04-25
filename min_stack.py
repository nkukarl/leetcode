class MinStack(object):
    def __init__(self):
        self.seq_min = []
        self.seq = []

    def push(self, x):
        if 0 == len(self.seq_min):
            self.seq_min.append(x)
        else:
            self.seq_min.append(min(self.seq_min[-1], x))
        self.seq.append(x)

    def pop(self):
        self.seq_min.pop()
        return self.seq.pop()

    def top(self):
        return self.seq[-1]

    def get_min(self):
        return self.seq_min[-1]
