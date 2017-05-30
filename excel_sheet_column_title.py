class Solution(object):
    def convert_to_title(self, n):
        if 0 == n:
            return ''
        return self.convert_to_title((n - 1) // 26) + \
               chr((n - 1) % 26 + ord('A'))
