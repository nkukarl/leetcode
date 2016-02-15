class Solution:
	def candy(self, A):
		C = [1] * len(A)
		for i in range(1, len(A)):
			if A[i] > A[i - 1]:
				C[i] = C[i - 1] + 1
		for i in range(len(A) - 2, -1, -1):
			if A[i] > A[i + 1]:
				C[i] = max(C[i], C[i + 1] + 1)
		return sum(C)

A = [1, 2, 2, 1, 3, 4, 2, 1, 4, 3]

inst = Solution()
print(inst.candy(A))