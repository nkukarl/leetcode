class Solution:
	def grayCode(self, n):
		if n == 1:
			return [0, 1]
		tmp = self.grayCode(n - 1)
		for i in range(len(tmp) - 1, -1, -1):
			tmp.append(2 ** (n - 1) + tmp[i])
		return tmp

inst = Solution()
print(inst.grayCode(4))