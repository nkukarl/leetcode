class Solution(object):
    def get_continuous_subset(self, nums, subtotal):
        cache = {0: -1}
        current = 0
        for i, n in enumerate(nums):
            current += n
            if current - subtotal in cache:
                return [cache[current - subtotal] + 1, i]
            cache[current] = i
