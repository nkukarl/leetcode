class Solution:
	def maxArea(self, height):
		if not height:
			return 0
		left, right = 0, len(height) - 1
		maxArea = 0
		while left < right:
			L, R = height[left], height[right]
			maxArea = max(maxArea, (right - left) * min(L, R))
			if L < R:
				left += 1
			elif L > R:
				right -= 1
			else:
				left += 1
				right -= 1

		return maxArea

height = [1, 3, 4, 9, 5, 2, 6, 1]

inst = Solution()
print(inst.maxArea(height))