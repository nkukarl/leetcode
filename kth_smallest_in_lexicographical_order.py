# TODO: Fix TLE when n = 4289384 and k = 1922239
class Solution(object):
    def find_kth_number(self, n, k):
        self.MAX = int('9' * (len(str(n)) + 1))
        self.nums = [i for i in range(1, n + 1)]
        self.heapify()
        while k > 1:
            self.pop_current_min()
            k -= 1
        return self.pop_current_min()

    def heapify(self):
        k = len(self.nums) // 2 - 1
        while k >= 0:
            self.sift_down(k)
            k -= 1

    def pop_current_min(self):
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        min_ = self.nums.pop()
        if len(self.nums) > 0:
            self.sift_down(0)
        return min_

    def sift_down(self, k):
        while True:
            n = self.nums[k]
            left, right = k * 2 + 1, k * 2 + 2
            n_left = self.nums[left] if left < len(self.nums) else self.MAX
            n_right = self.nums[right] if right < len(self.nums) else self.MAX
            if self.compare(n_left, n) and self.compare(n_right, n):
                break
            if self.compare(n_left, n_right):
                self.nums[k], self.nums[right] = self.nums[right], self.nums[k]
                k = right
            else:
                self.nums[k], self.nums[left] = self.nums[left], self.nums[k]
                k = left

    def compare(self, m, n):
        """

        If m is greater than n in lexicographical order, return True.
        Otherwise, return False.

        Args:
            m (int):
            n (int):

        Returns:
            bool

        """
        if len(str(m)) == len(str(n)):
            return m > n
        m, n = list(map(int, str(m))), list(map(int, str(n)))
        for i in range(max(len(m), len(n))):
            m_ = m[i] if i < len(m) else None
            n_ = n[i] if i < len(n) else None
            if m_ == n_:  # m_ and n_ cannot be both None
                continue
            if m_ is None:
                return False
            if n_ is None:
                return True
            return m_ > n_
