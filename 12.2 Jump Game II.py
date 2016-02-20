class Solution:
	def jump(self, A):
		if len(A) == 1:
			return 0
		left, right = 0, A[0]
		step = 1
		curPos = 0
		while right < len(A) - 1:
			step += 1
			for p in range(left, right + 1):
				curPos = max(curPos, p + A[p])
			right = curPos

		return step

A = [2, 3, 1, 1, 4]
A = [2, 0, 1, 4, 3]

inst = Solution()
print(inst.jump(A))