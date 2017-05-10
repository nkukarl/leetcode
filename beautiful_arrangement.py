class Solution(object):
    def count_arrangement(self, N):
        self.count = 0
        nums = [i for i in range(1, N + 1)]
        self.build(nums, [0])
        return self.count

    def build(self, nums, cur):
        if 0 == len(nums):
            self.count += 1
            return
        length = len(cur)
        for i, n in enumerate(nums):
            if 0 in [n % length, length % n]:
                self.build(nums[:i] + nums[i + 1:], cur + [n])
