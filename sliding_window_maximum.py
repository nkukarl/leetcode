from utils_dequeue import Dequeue


class Solution(object):
    def max_sliding_window(self, nums, k):
        dequeue, ans = Dequeue(), []
        for i, n in enumerate(nums):
            while not dequeue.is_empty() and n > nums[dequeue.get(-1)]:
                dequeue.pop()
            dequeue.append(i)
            if i - k == dequeue.get(0):
                dequeue.pop_left()
            if i >= k - 1:
                ans.append(nums[dequeue.get(0)])
        return ans
