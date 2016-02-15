class Solution:
	def singleNumber(self, A):
		summary = [0] * 32
		for n in A:
			if n < 0:
				n = (1 << 32) + n
			counter = 0
			while n and counter < 32:
				summary[counter] += n & 1
				n >>= 1
				counter += 1
		print(summary)
		val = 1
		res = 0

		for s in summary:
			if s % 3 != 0:
				res += val
			val <<= 1
		if summary[-1] % 3 != 0:
			res -= 2 ** 32
		return res

A = [1] * 3 + [2] * 3 + [-5] * 3 + [-6]
inst = Solution()

print(inst.singleNumber(A))