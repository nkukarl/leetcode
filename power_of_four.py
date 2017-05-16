class Solution(object):
    def is_power_of_four(self, num):
        # num must be a positive integer
        if num <= 0:
            return False
        # num must be a power of two
        if num & (num - 1) != 0:
            return False
        return num & 0x55555555 != 0

        # One-liner
        # return num > 0 and 0 == num & (num - 1) and num & 0x55555555 != 0
