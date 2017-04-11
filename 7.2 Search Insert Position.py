class Solution:
    def searchInsert(self, A, target):
        if target <= A[0]:
            return 0
        if target > A[-1]:
            return len(A)
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


A = [1, 3, 5, 6]
target = 7

inst = Solution()
print(inst.searchInsert(A, target))
