class MaxHeap(object):
    def __init__(self, size, MIN_INT):
        self.size = size
        self.MIN_INT = MIN_INT
        self.pairs = []

    def is_empty(self):
        return 0 == len(self.pairs)

    def push(self, pair):
        if len(self.pairs) == self.size:
            total, _, _ = pair
            if total >= self.pairs[0][0]:
                return
            self.pairs[0] = pair
            self.sift_down(0)
        else:
            self.pairs.append(pair)
            self.sift_up(len(self.pairs) - 1)

    def pop(self):
        self.pairs[0], self.pairs[-1] = self.pairs[-1], self.pairs[0]
        pair = self.pairs.pop()
        self.sift_down(0)
        return pair

    def sift_up(self, cur_id):
        while cur_id > 0:
            parent_id = (cur_id - 1) // 2
            parent_total = self.pairs[parent_id][0]
            if self.pairs[cur_id][0] > parent_total:
                self.pairs[cur_id], self.pairs[parent_id] = \
                    self.pairs[parent_id], self.pairs[cur_id]
            else:
                break
            cur_id = parent_id

    def sift_down(self, cur_id):
        while cur_id < len(self.pairs) // 2:
            left_child_id = 2 * cur_id + 1
            right_child_id = 2 * cur_id + 2
            # Given i < len(self.pairs) // 2, left_child always exists.
            left_total = self.pairs[left_child_id][0]
            if right_child_id >= len(self.pairs):
                right_total = self.MIN_INT
            else:
                right_total = self.pairs[right_child_id][0]
            current_val = self.pairs[cur_id][0]
            if left_total <= current_val >= right_total:
                break
            if left_total > right_total:
                self.pairs[cur_id], self.pairs[left_child_id] = \
                    self.pairs[left_child_id], self.pairs[cur_id]
                cur_id = left_child_id
            else:
                self.pairs[cur_id], self.pairs[right_child_id] = \
                    self.pairs[right_child_id], self.pairs[cur_id]
                cur_id = right_child_id


class Solution(object):
    def k_smallest_pairs(self, nums1, nums2, k):
        """
        Basically, we are maintaining a max heap with size of less than or
        equal to k.
        For each pair, push it to the heap.
        After looping through the pairs, pop each element in the heap
        and return them in the reverse order.
        
        This solution does not require nums1 or nums2 to be sorted,
        which is a more generic solution.
        However, given that nums1 and nums2 are sorted, there should
        be room for further improvement.
        """
        if 0 in [len(nums1), len(nums2)]:
            return []
        MIN_INT = min(nums1) + min(nums2) - 1
        max_heap = MaxHeap(k, MIN_INT)
        for m in nums1:
            for n in nums2:
                pair = (m + n, m, n)
                max_heap.push(pair)

        ans = []
        while not max_heap.is_empty():
            total, m, n = max_heap.pop()
            ans.append([m, n])

        return ans[::-1]