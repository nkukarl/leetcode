class Solution(object):
    def top_k_frequent(self, nums, k):
        self.summarise(nums)
        self.heapify()
        elements = []
        while k > 0:
            _, element = self.pop_current_top_element()
            elements.append(element)
            k -= 1
        return elements

    def summarise(self, nums):
        summary_raw = dict()
        for n in nums:
            summary_raw[n] = summary_raw.get(n, 0) + 1
        self.summary = []
        for k, v in summary_raw.items():
            self.summary.append((v, k))
        return self.summary

    def heapify(self):
        index = len(self.summary) // 2 - 1
        while index >= 0:
            self.sift_down(index)
            index -= 1

    def pop_current_top_element(self):
        self.summary[0], self.summary[-1] = self.summary[-1], self.summary[0]
        element = self.summary.pop()
        if len(self.summary) > 0:
            self.sift_down(0)
        return element

    def sift_down(self, index):
        while True:
            tup = self.summary[index]
            left, right = index * 2 + 1, index * 2 + 2
            tup_left = \
                self.summary[left] if left < len(self.summary) else (0, 0)
            tup_right = \
                self.summary[right] if right < len(self.summary) else (0, 0)
            if tup_left[0] < tup[0] > tup_right[0]:
                break
            if tup_left[0] < tup_right[0]:
                self.summary[index], self.summary[right] = \
                    self.summary[right], self.summary[index]
                index = right
            else:
                self.summary[index], self.summary[left] = \
                    self.summary[left], self.summary[index]
                index = left
