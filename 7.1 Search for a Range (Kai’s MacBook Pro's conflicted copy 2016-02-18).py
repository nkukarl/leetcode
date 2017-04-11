class Solution:
    def searchRange(self, A, target):
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid + 1
            else:
                right = mid
        if A[left] != target:
            return [-1, -1]

        start = left

        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < target + 1:
                left = mid + 1
            else:
                right = mid

        end = max(left - 1, start)

        return [start, end]


A = [5, 6, 7, 7, 8, 8, 10]

inst = Solution()
print(inst.searchRange(A, 8))
