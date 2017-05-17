class Solution(object):
    def matrix_reshape(self, nums, r, c):
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        ans = [[0] * c for _ in range(r)]
        for pos in range(r * c):
            ans[pos // c][pos % c] = nums[pos // n][pos % n]
        return ans
