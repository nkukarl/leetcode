# TODO: Fix TLE
class Solution(object):
    def triangle_number(self, nums):
        nums.sort()
        m = len(nums)
        count = 0
        cache_valid, cache_invalid = set(), set()
        for i in range(m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    sides = nums[i], nums[j], nums[k]
                    if sides in cache_valid:
                        count += 1
                        continue
                    if sides in cache_invalid:
                        continue
                    is_valid = self.is_valid_triplet(sides)
                    if is_valid:
                        cache_valid.add(sides)
                        count += 1
                    else:
                        cache_invalid.add(sides)

        return count

    def is_valid_triplet(self, sides):
        a, b, c = sides
        return a + b > c and abs(a - b) < c
