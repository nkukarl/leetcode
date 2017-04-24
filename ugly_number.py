class Solution(object):
    def is_ugly(self, num):
        if num <= 0:
            return False
        if 1 == num:
            return True
        for p in [2, 3, 5]:
            while 0 == num % p:
                num //= p
        return 1 == num
