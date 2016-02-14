class Solution:
	def removeElement(self, A, target):
		left, right = 0, len(A) - 1
		while left < right:
			while left < right and A[left] != target:
				left += 1
			while left < right and A[right] == target:
				right -= 1
			if left < right:
				A[left], A[right] = A[right], A[left]
				left += 1
				right -= 1
		return left + 1

A = [1, 3, 4, 2, 5, 9, 2, 6, 1, 7, 3, 2]
target = 2

inst = Solution()
length = inst.removeElement(A, target)

print(A)
print(A[:length])