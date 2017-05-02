# TODO: Anything more efficient?
class Solution(object):
    def kth_smallest(self, matrix, k):
        if 0 == len(matrix):
            return None
        cc = len(matrix[0])
        if 0 == cc:
            return None
        self.MAX = 2 ** 31
        self.elements = []
        for i, row in enumerate(matrix):
            self.elements.append((row[0], i, 0))
        self.heapify()
        while k > 1:
            _, r, c = self.pop_current_min()
            if c + 1 < cc:
                self.add_element((matrix[r][c + 1], r, c + 1))
            k -= 1
        num, _, _ = self.pop_current_min()
        return num

    def heapify(self):
        index = len(self.elements) // 2 - 1
        while index >= 0:
            self.sift_down(index)
            index -= 1

    def pop_current_min(self):
        self.elements[0], self.elements[-1] = \
            self.elements[-1], self.elements[0]
        ans = self.elements.pop()
        if len(self.elements) > 0:
            self.sift_down(0)
        return ans

    def add_element(self, element):
        self.elements.append(element)
        self.sift_up(len(self.elements) - 1)

    def sift_up(self, index):
        while (index - 1) // 2 >= 0:
            index_parent = (index - 1) // 2
            if self.elements[index_parent][0] < self.elements[index][0]:
                break
            self.elements[index], self.elements[index_parent] = \
                self.elements[index_parent], self.elements[index]
            index = index_parent

    def sift_down(self, index):
        while True:
            n = self.elements[index][0]
            left, right = index * 2 + 1, index * 2 + 2
            left_n = self.elements[left][0] \
                if left < len(self.elements) else self.MAX
            right_n = self.elements[right][0] \
                if right < len(self.elements) else self.MAX
            if left_n > n < right_n:
                break
            if left_n < right_n:
                self.elements[index], self.elements[left] = \
                    self.elements[left], self.elements[index]
                index = left
            else:
                self.elements[index], self.elements[right] = \
                    self.elements[right], self.elements[index]
                index = right
