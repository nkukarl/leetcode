class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.cache = []

    def peek(self):
        if 0 == len(self.cache):
            self.cache.append(self.iterator.get_next())
        return self.cache[0]

    def get_next(self):
        if len(self.cache) > 0:
            return self.cache.pop()
        return self.iterator.get_next()

    def has_next(self):
        return len(self.cache) > 0 or self.iterator.has_next()
