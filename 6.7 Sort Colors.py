class Solution:
    def sortColors(self, A):
        left, right = 0, len(A) - 1
        i = 0
        while i <= right:
            if A[i] == 0:
                A[i], A[left] = A[left], A[i]
                left += 1
                i += 1
            elif A[i] == 2:
                A[i], A[right] = A[right], A[i]
                right -= 1
            else:
                i += 1


import random

A = [0, 1, 2] * 5
random.shuffle(A)

print(A)

inst = Solution()
inst.sortColors(A)

print(A)
