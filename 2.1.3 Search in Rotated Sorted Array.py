class Solution:
	def search(self, A, target):
		left, right = 0, len(A) - 1
		while left < right:
			mid = (left + right) // 2
			if A[mid] > A[right]:
				left = mid + 1
			else:
				right = mid
		pivot = left
		B, C = A[:pivot], A[pivot:]
		b = self.binarySearch(B, target)
		c = self.binarySearch(C, target)

		if c == -1:
			return b
		return c + pivot

	def binarySearch(self, A, target):
		if not A:
			return -1
		if target < A[0]:
			return -1
		if target > A[-1]:
			return -1
		left, right = 0, len(A) - 1
		while left < right:
			mid = (left + right) // 2
			if A[mid] < target:
				left = mid + 1
			else:
				right = mid
		if A[left] == target:
			return left
		return -1

A = [4, 5, 6, 7, 0, 1, 2]

inst = Solution()
print(inst.search(A, 5))