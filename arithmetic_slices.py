class Solution(object):
    def number_of_arithmetic_slices(self, nums):
        if len(nums) < 3:
            return 0
        diffs = [n1 - n2 for n1, n2 in zip(nums[1:], nums[:-1])]
        counts = []

        cur = diffs[0]
        count = 1
        for diff in diffs[1:]:
            if diff == cur:
                count += 1
            else:
                if count > 1:
                    counts.append(count + 1)
                cur = diff
                count = 1
        if count > 1:
            counts.append(count + 1)

        ans = 0
        for count in counts:
            ans += ((count - 2) + 1) * (count - 2) // 2

        return ans
