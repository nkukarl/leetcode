class Solution:
	def trap(self, A):
		L = self.highestBarLeft(A)
		R = self.highestBarLeft(A[::-1])[::-1]

		area = 0

		for i in range(len(A)):
			H = min(L[i], R[i])
			h = A[i]
			area += max(0, H - h)

		return area

	def highestBarLeft(self, A):
		ans = [0]
		curMax = A[0]
		for h in A[1:]:
			ans.append(curMax)
			curMax = max(curMax, h)
		return ans

A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

inst = Solution()
print(inst.trap(A))