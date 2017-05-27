class Solution(object):
    def product_except_self(self, nums):
        if 0 == len(nums):
            return []

        l2r, r2l = [1], [1]
        for n in nums[:-1]:
            l2r.append(l2r[-1] * n)
        for n in nums[:0:-1]:
            r2l.append(r2l[-1] * n)
        r2l = r2l[::-1]

        return [n1 * n2 for n1, n2 in zip(l2r, r2l)]
