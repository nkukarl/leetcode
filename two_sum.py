class Solution:
    def two_sum(self, numbers, target):
        cache = dict()
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            if new_target in cache:
                return [cache[new_target], i]
            cache[numbers[i]] = i
