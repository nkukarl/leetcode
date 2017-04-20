class Solution:
    def combination_sum_ii(self, numbers, target):
        numbers.sort()
        self.target = target
        self.res = set()
        self.helper(numbers, tuple())

        return [list(r) for r in self.res]

    def helper(self, numbers, cur):
        if sum(cur) == self.target:
            self.res.add(cur)
        elif sum(cur) < self.target:
            for i in range(len(numbers)):
                self.helper(numbers[i + 1:], cur + (numbers[i],))
