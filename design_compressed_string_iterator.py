class StringIterator(object):
    def __init__(self, compressed_string):
        self.string = compressed_string
        self.cur = ''
        self.count = 0
        self.pos = 0

    def next(self):
        if not self.has_next():
            return ' '

        if 0 == self.count:
            self.cur = self.string[self.pos]
            self.pos += 1
            while self.pos < len(self.string) \
                    and self.string[self.pos] in '0123456789':
                self.count = self.count * 10 + int(self.string[self.pos])
                self.pos += 1

        self.count -= 1
        return self.cur

    def has_next(self):
        return self.pos < len(self.string) or self.count > 0
