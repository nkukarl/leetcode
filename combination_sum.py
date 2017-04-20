class Solution:
    def combination_sum(self, numbers, target):
        numbers = list(set(numbers))
        numbers.sort()
        self.target = target
        self.res = []
        self.helper(numbers, [])

        return self.res

    def helper(self, numbers, cur):
        if sum(cur) == self.target:
            self.res.append(cur)
        elif sum(cur) < self.target:
            for i in range(len(numbers)):
                self.helper(numbers[i:], cur + [numbers[i]])
