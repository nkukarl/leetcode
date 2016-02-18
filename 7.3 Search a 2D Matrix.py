class Solution:
	def searchMatrix(self, M, target):
		m, n = len(M), len(M[0])
		top, bottom = 0, m - 1
		while top < bottom:
			mid = (top + bottom) // 2
			if M[mid][-1] < target:
				top = mid + 1
			else:
				bottom = mid
		left, right = 0, n - 1
		while left < right:
			mid = (left + right) // 2
			if M[top][mid] < target:
				left = mid + 1
			else:
				right = mid
		return M[top][left] == target

M = [[1, 3, 5, 7], [8, 9, 11, 14], [17, 21, 24, 27], [35, 49, 77, 89]]
target = 12
inst = Solution()
print(inst.searchMatrix(M, target))