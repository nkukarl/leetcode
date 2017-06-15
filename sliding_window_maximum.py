class Solution(object):
    def max_sliding_window(self, nums, k):
        dequeue, ans = [], []
        for i, n in enumerate(nums):
            while dequeue and n > nums[dequeue[-1]]:
                dequeue.pop()
            dequeue.append(i)
            if i - k == dequeue[0]:
                dequeue.pop(0)
            if i >= k - 1:
                ans.append(nums[dequeue[0]])
        return ans
