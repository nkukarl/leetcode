class Solution:
	def singleNumber(self, A):
		tmp = 0
		for n in A:
			tmp ^= n
		return n

A = [1, 1, 2, 3, 3, 2, 4]

inst = Solution()
print(inst.singleNumber(A))