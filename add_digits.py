class Solution(object):
    def add_digits(self, num):
        if 0 == num:
            return 0
        if 0 == num % 9:
            return 9
        return num % 9
