class Solution:
    def three_sum(self, numbers, target):
        numbers.sort()
        res = []
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                triplet = [numbers[i], numbers[j], numbers[k]]
                total = sum(triplet)
                if total == target:
                    res.append(triplet)
                    while j < k and numbers[j] == numbers[j + 1]:
                        j += 1
                    while j < k and numbers[k] == numbers[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    k -= 1
        return res
