class Solution:
    def three_sum(self, numbers, target):
        numbers.sort()
        res = set()
        for i in range(len(numbers) - 2):
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                collection = (numbers[i], numbers[j], numbers[k])
                if sum(collection) == target:
                    res.add(collection)
                    j += 1
                    k -= 1
                elif sum(collection) < target:
                    j += 1
                else:
                    k -= 1
        return [list(r) for r in res]
