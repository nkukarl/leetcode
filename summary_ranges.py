class Solution(object):
    def summary_ranges(self, nums):
        if len(nums) < 2:
            return list(map(str, nums))
        cur = [nums[0]]
        ranges_raw = []
        for n in nums[1:]:
            if cur[-1] + 1 == n:
                cur.append(n)
            else:
                ranges_raw.append(cur)
                cur = [n]
        ranges_raw.append(cur)
        ranges = []
        for r_r in ranges_raw:
            if len(r_r) > 1:
                ranges.append(str(r_r[0]) + '->' + str(r_r[-1]))
            else:
                ranges.append(str(r_r[0]))
        return ranges
