class Solution(object):
    def third_max(self, nums):
        if 0 == len(nums):
            raise ValueError
        if len(nums) < 3:
            return max(nums)
        self.MIN = min(nums) - 1
        self.nums = nums
        self.heapify()
        top_3 = [self.pop_current_max()]
        while self.nums and len(top_3) < 3:
            max_ = self.pop_current_max()
            if top_3[-1] != max_:
                top_3.append(max_)
        if len(top_3) < 3:
            return top_3[0]
        return top_3[-1]

    def heapify(self):
        k = len(self.nums) // 2 - 1
        while k >= 0:
            self.sift_down(k)
            k -= 1

    def pop_current_max(self):
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        max_ = self.nums.pop()
        if len(self.nums) > 0:
            self.sift_down(0)
        return max_

    def sift_down(self, k):
        while True:
            n = self.nums[k]
            left, right = k * 2 + 1, k * 2 + 2
            n_left = self.nums[left] if left < len(self.nums) else self.MIN
            n_right = self.nums[right] if right < len(self.nums) else self.MIN
            if n_left < n > n_right:
                break
            if n_left < n_right:
                self.nums[k], self.nums[right] = self.nums[right], self.nums[k]
                k = right
            else:
                self.nums[k], self.nums[left] = self.nums[left], self.nums[k]
                k = left
