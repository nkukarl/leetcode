class Solution(object):
    def print_diamond(self, n):
        self.max_n = n
        print()
        self._print(1)

    def _print(self, n):
        print((self.max_n - n) // 2 * ' ' + n * '*')
        if n != self.max_n:
            self._print(n + 2)
            print((self.max_n - n) // 2 * ' ' + n * '*')
