class Solution:
	def nextPermutation(self, A):
		pivot = None
		for i in range(len(A) - 1, 0, -1):
			if A[i] > A[i - 1]:
				pivot = i - 1
				break
		if pivot == None:
			A.reverse()
		else:
			curVal = A[pivot + 1]
			curIdx = pivot + 1
			for i in range(curIdx + 1, len(A)):
				if A[i] > A[pivot] and A[i] < curVal:
					curVal = A[i]
					curIdx = i
			A[pivot], A[curIdx] = A[curIdx], A[pivot]
			self.partialReverse(A, pivot + 1, len(A) - 1)

	def partialReverse(self, A, left, right):
		while left < right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1

A = [1, 4, 2, 6, 5, 7, 6, 3]
A = [1, 2, 3, 4]
A = [4, 3, 2, 1]

inst = Solution()
inst.nextPermutation(A)

print(A)