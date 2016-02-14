class Solution:
	def longestConsecutive(self, A):
		A = list(set(A))
		summary = dict()
		for n in A:
			summary[n] = 1
		maxLen = 1
		for n in A:
			low = n - 1
			while low in summary:
				del summary[low]
				low -= 1
			high = n + 1
			while high in summary:
				del summary[high]
				high += 1
			maxLen = max(maxLen, high - low - 1)
		return maxLen

A = [100, 4, 200, 1, 3, 2, 5, 6]

inst = Solution()
print(inst.longestConsecutive(A))