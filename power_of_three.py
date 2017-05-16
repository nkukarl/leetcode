class Solution(object):
    def is_power_of_three(self, num):
        return num > 0 and 0 == 3 ** 19 % num
