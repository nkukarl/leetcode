class Solution:
	def maximalRectangle(self, M):
		if not M:
			return 0
		m, n = len(M), len(M[0])
		height = [0] * n
		ans = 0
		for i in range(m):
			tmp = [0] * n
			for j in range(n):
				if M[i][j] == '1':
					tmp[j] = height[j] + 1
				else:
					tmp[j] = 0
			# print(tmp)
			ans = max(ans, self.helper(tmp))
			height = tmp[:]
		return ans

	def helper(self, height):
		height.append(0)
		stack = [-1]
		ans = 0
		for i in range(len(height)):
			h = height[i]
			while h < height[stack[-1]]:
				tmp = stack.pop()
				H = height[tmp]
				W = i - stack[-1] - 1
				ans = max(ans, H * W)
			stack.append(i)
		return ans

M = ['000', '010', '111']
# M = ['1']

inst = Solution()
print(inst.maximalRectangle(M))