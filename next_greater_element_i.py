class Solution(object):
    def next_greater_element(self, find_nums, nums):
        summary = {n: i for i, n in enumerate(nums)}
        ans = []
        for n in find_nums:
            id_ = summary[n]
            next_greater = -1
            for i in range(id_ + 1, len(nums)):
                if nums[i] > n:
                    next_greater = nums[i]
                    break
            ans.append(next_greater)

        return ans
