class Solution(object):
    def product_except_self(self, nums):
        if 0 == len(nums):
            return []

        # Handle simple scenario
        count_of_zero = nums.count(0)
        if count_of_zero >= 2:
            return [0] * len(nums)

        prod = 1
        pos = None
        for i, n in enumerate(nums):
            if n != 0:
                prod *= n
            else:
                pos = i

        if count_of_zero == 1:
            ans = [0] * len(nums)
            ans[pos] = prod
            return ans

        ans = []
        for n in nums:
            ans.append(prod // n)
        return ans
