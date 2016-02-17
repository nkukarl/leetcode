class Solution:
	def largestRectangleArea(self, height):
		height.append(0)
		stack = [-1]
		maxArea = 0
		for i in range(len(height)):
			h = height[i]
			while h < height[stack[-1]]:
				tmp = stack.pop()
				print((i - tmp) * height[tmp])
				maxArea = max(maxArea, (i - stack[-1] - 1) * height[tmp])
			stack.append(i)
		return maxArea

height = [2, 1, 5, 6, 2, 3]
height = [2, 2, 3, 4, 1, 2]
inst = Solution()
print(inst.largestRectangleArea(height))