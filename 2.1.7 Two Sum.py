class Solution:
	def twoSum(self, A, target):
		MAP = dict()
		for i in range(len(A)):
			newTarget = target - A[i]
			if newTarget in MAP:
				return [MAP[newTarget] + 1, i + 1]
			MAP[A[i]] = i

A = [2, 7, 11, 15]
target = 17

inst = Solution()
print(inst.twoSum(A, target))
