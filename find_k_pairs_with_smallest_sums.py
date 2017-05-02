# TODO: Fix TLE
class Solution(object):
    def k_smallest_pairs(self, nums1, nums2, k):
        if 0 in [len(nums1), len(nums2)]:
            return []
        self.pairs = []
        self.MAX = nums1[0] + nums2[0] + 1
        for n1 in nums1:
            for n2 in nums2:
                sum_ = n1 + n2
                self.pairs.append((sum_, [n1, n2]))
                self.MAX = max(self.MAX, sum_ + 1)
        self.heapify()
        pairs = []
        while k > 0 and len(self.pairs) > 0:
            pairs.append(self.pop_current_min())
            k -= 1
        return pairs

    def pop_current_min(self):
        self.pairs[0], self.pairs[-1] = self.pairs[-1], self.pairs[0]
        _, pair = self.pairs.pop()
        if len(self.pairs) > 0:
            self.sift_down(0)
        return pair

    def heapify(self):
        index = len(self.pairs) // 2 - 1
        while index >= 0:
            self.sift_down(index)
            index -= 1

    def sift_down(self, index):
        while True:
            sum_ = self.pairs[index][0]
            left, right = index * 2 + 1, index * 2 + 2
            sum_left = self.pairs[left][0] \
                if left < len(self.pairs) else self.MAX
            sum_right = self.pairs[right][0] \
                if right < len(self.pairs) else self.MAX
            if sum_left > sum_ < sum_right:
                break
            if sum_left < sum_right:
                self.pairs[index], self.pairs[left] = \
                    self.pairs[left], self.pairs[index]
                index = left
            else:
                self.pairs[index], self.pairs[right] = \
                    self.pairs[right], self.pairs[index]
                index = right
