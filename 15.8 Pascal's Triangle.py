class Solution:
	def generate(self, n):
		if n == 1:
			return [[1]]
		ans = [[1]]
		for i in range(1, n):
			tmp = [1] + [0] * (i - 1) + [1]
			for j in range(1, i):
				tmp[j] = ans[-1][j - 1] + ans[-1][j]
			ans.append(tmp)
		return ans

inst = Solution()
print(inst.generate(5))