class Solution:
    def single_number(self, numbers):
        mark = 0
        for n in numbers:
            mark ^= n
        return mark
