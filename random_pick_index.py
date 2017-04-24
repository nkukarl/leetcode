import random


class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res


class SolutionWithCache(object):
    def __init__(self, nums):
        self.nums = nums
        self.cache = {}

    def pick(self, target):
        if target not in self.cache:
            res = []
            for i, num in enumerate(self.nums):
                if num == target:
                    res.append(i)
            self.cache[target] = res
        return random.choice(self.cache[target])


class SolutionSummariseWhenInitialised(object):
    def __init__(self, nums):
        self.summary = summary = {}
        for i, num in enumerate(nums):
            entry = summary.get(num)
            if entry is None:
                summary[num] = i
            elif isinstance(entry, int):
                summary[num] = [entry, i]
            else:
                summary[num].append(i)

    def pick(self, target):
        res = self.summary[target]
        return res if isinstance(res, int) else random.choice(res)
