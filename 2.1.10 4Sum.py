class Solution:
	def fourSum(self, A, target):
		if len(A) < 4:
			return False
		A.sort()
		res = set()
		summary = dict()
		for i in range(len(A)):
			for j in range(i + 1, len(A)):
				tmp = A[i] + A[j]
				summary[tmp] = summary.get(tmp, []) + [[i, j]]
		for k in summary:
			if target - k in summary:
				C = summary[k]
				D = summary[target - k]
				for c in C:
					for d in D:
						if c[0] != d[0] and c[0] != d[1] and c[1] != d[0] and c[1] != d[1]:
							ans = [A[c[0]], A[c[1]], A[d[0]], A[d[1]]]
							ans.sort()
							res.add(tuple(ans))

		return [list(r) for r in res]

A = [1, 0, -1, 0, -2, 2]
target = 0

inst = Solution()
print(inst.fourSum(A, target))


