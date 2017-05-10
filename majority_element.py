class Solution(object):
    def majority_element(self, nums):
        el = nums[0]
        count = 1
        for n in nums[1:]:
            if n == el:
                count += 1
            else:
                count -= 1
                if -1 == count:
                    el = n
                    count = 1
        return el