class Solution:
	def threeSum(self, A, target):
		A.sort()
		res = set()
		for i in range(len(A) - 2):
			j = i + 1
			k = len(A) - 1
			while j < k:
				tmp = (A[i], A[j], A[k])
				if sum(tmp) == target:
					res.add(tmp)
					j += 1
					k -= 1
				elif sum(tmp) < target:
					j += 1
				else:
					k -= 1
		return [list(r) for r in res]

A = [-1, 0, 1, 2, -1, 4]
target = 0

inst = Solution()
print(inst.threeSum(A, target))




