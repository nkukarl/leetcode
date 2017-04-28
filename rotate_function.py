class Solution(object):
    def max_rotate_function(self, nums):
        """

        nums = [4, 3, 2, 6]
        base_value = F(0)
        o < < < < < < < < < < < < < < < < < < < < o
        v                                         ^
        v                                         ^
        v   F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
        v           v         v         v
        v           v         v         v
        v           v         v         v +nums[2]
        v           v         v         o > > > > o
        v           v         v                   v
        v           v         v +nums[1]          v
        v           v         o > > > > o         v
        v           v                   v         v
        v           v +nums[0]          v         v
        v           o > > > > o         v         v
        v                     v         v         v
        v -nums[3] * 3        v         v         v
        o > > > > > o         v         v         v
                    v         v         v         v
                    v         v         v         v
                    v         v         v         v
            F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16

            From F(0) to F(1),
            diff = nums[0] + nums[1] + nums[2] - nums[3] * 3
                 = nums[0] + nums[1] + nums[2] + nums[3] - nums[3] * 4
                 = sum(nums) - nums[-1] * len(nums)

            F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23

            Similarly, from F(1) to F(2),
            diff = sum(nums) - nums[-2] * len(nums)

            F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26


        """
        if 0 == len(nums):
            return 0
        sum_value = sum(nums)
        count = len(nums)
        base_value = sum([i * n for i, n in enumerate(nums)])
        max_value = base_value
        for index in range(-1, -count, -1):
            diff = sum_value - count * nums[index]
            base_value += diff
            max_value = max(max_value, base_value)
        return max_value
