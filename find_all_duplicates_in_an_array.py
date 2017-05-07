class Solution(object):
    def find_duplicates(self, nums):
        duplicates = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                duplicates.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return duplicates
