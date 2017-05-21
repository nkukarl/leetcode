class Solution(object):
    def summary_ranges(self, nums):
        if len(nums) < 2:
            return list(map(str, nums))
        start, end = nums[0], None
        ranges = []
        for n in nums[1:]:
            if end is None:
                if n == start + 1:
                    end = n
                else:
                    ranges.append(str(start))
                    start = n
            else:
                if n == end + 1:
                    end = n
                else:
                    ranges.append(str(start) + '->' + str(end))
                    start, end = n, None
        if end is None:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + '->' + str(end))
        return ranges
