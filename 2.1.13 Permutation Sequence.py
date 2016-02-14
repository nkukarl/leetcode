class Solution:
	def getPermutation(self, n, k):
		factorial = [1]
		for i in range(1, n):
			factorial.append(factorial[-1] * i)
		k -= 1
		m = n - 1
		A = [i for i in range(1, n + 1)]
		res = []
		while m >= 0:
			idx = k // factorial[m]
			k %= factorial[m]
			res.append(A[idx])
			A.pop(idx)
			m -= 1
		return res

n, k = 5, 10

inst = Solution()
print(inst.getPermutation(n, k))
