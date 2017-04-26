class Solution(object):
    def permute(self, nums):
        self.seqs = []
        self.traverse(nums, [])
        return self.seqs

    def traverse(self, nums, cur):
        if 0 == len(nums):
            self.seqs.append(cur)
        else:
            for i, num in enumerate(nums):
                self.traverse(nums[:i] + nums[i + 1:], cur + [num])

    def permute_unique(self, nums):
        self.sets = set()
        self.traverse_unique(nums, [])
        return [list(s) for s in self.sets]

    def traverse_unique(self, nums, cur):
        if 0 == len(nums):
            self.sets.add(tuple(cur))
        else:
            for i, num in enumerate(nums):
                self.traverse_unique(nums[:i] + nums[i + 1:], cur + [num])
