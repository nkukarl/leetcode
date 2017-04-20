class Solution:
    def remove_element(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            while left < right and numbers[left] != target:
                left += 1
            while left < right and numbers[right] == target:
                right -= 1
            if left < right:
                numbers[left], numbers[right] = \
                    numbers[right], numbers[left]
                left += 1
                right -= 1
        return left + 1
