class Solution(object):
    def find_kth_largest(self, nums, k):
        if k > len(nums):
            raise ValueError
        # Let MIN be min(nums) - 1 for use in sift_down method
        self.MIN = min(nums) - 1
        self.nums = nums
        self.heapify()
        while k > 1:
            self.pop_current_max()
            k -= 1
        return self.pop_current_max()

    def heapify(self):
        k = len(self.nums) // 2 - 1
        while k >= 0:
            self.sift_down(k)
            k -= 1

    def pop_current_max(self):
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        max_ = self.nums.pop()
        self.sift_down(0)
        return max_

    def sift_down(self, k):
        while len(self.nums) > 0:
            n = self.nums[k]
            left = k * 2 + 1
            right = k * 2 + 2
            # If left or right child does not exist, assume their values
            # are smaller than that of parent by letting the values be MIN.
            n_left = self.nums[left] if left < len(self.nums) else self.MIN
            n_right = self.nums[right] if right < len(self.nums) else self.MIN
            # If the value of parent is greater than both children,
            # stop sifting down.
            if n_left < n > n_right:
                break
            # Swap the value of parent with the child with larger value
            if n_left < n_right:
                self.nums[k], self.nums[right] = self.nums[right], self.nums[k]
                k = right
            else:
                self.nums[k], self.nums[left] = self.nums[left], self.nums[k]
                k = left
