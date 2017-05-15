class Solution(object):
    def total_hamming_distance(self, nums):
        BITS = 32
        counts = [[0, 0] for _ in range(BITS)]
        for n in nums:
            for i in range(BITS):
                if 0 == n & 1:
                    counts[i][0] += 1
                else:
                    counts[i][1] += 1
                n >>= 1
        total_dist = 0
        for count in counts:
            total_dist += count[0] * count[1]
        return total_dist
