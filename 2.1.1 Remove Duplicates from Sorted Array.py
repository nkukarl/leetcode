class Solution:
	def removeDuplicates(self, A):
		if len(A) <= 1:
			return len(A)
		slow, fast = 0, 1
		n = len(A)
		while fast < n:
			while fast < n and A[fast] == A[slow]:
				fast += 1
			if fast < n:
				slow += 1
				A[slow], A[fast] = A[fast], A[slow]
				fast += 1
		return slow

class Solution:
	def removeDuplicates(self, A):
		if len(A) <= 1:
			return len(A)
		n = len(A)
		pos = 0
		for i in range(1, n):
			if A[pos] != A[i]:
				pos += 1
				A[pos] = A[i]
		return pos + 1

A = [1] * 3 + [2] * 4 + [3] * 3

inst = Solution()
length = inst.removeDuplicates(A)

print(A[:length])