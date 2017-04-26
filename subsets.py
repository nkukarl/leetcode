class Solution(object):
    def subsets(self, nums):
        self.sets = [[]]
        self.traverse(nums, [])
        return self.sets

    def traverse(self, nums, cur):
        if len(nums) > 0:
            for i, num in enumerate(nums):
                next_ = cur + [num]
                self.sets.append(next_)
                self.traverse(nums[i + 1:], next_)
