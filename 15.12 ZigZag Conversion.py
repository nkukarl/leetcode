class Solution:
	def convert(self, s, n):
		if n == 1:
			return s
		tmp = []
		for i in range(n):
			tmp.append([])
		for i in range(len(s)):
			val = i % (2 * n - 2)
			if val > n - 1:
				tmp[2 * n - 2 - val].append(i)
			else:
				tmp[val].append(i)
		print(tmp)
		res = ''
		for row in tmp:
			for col in row:
				res += s[col]
		return res

s = 'paypalishiring'
n = 1

inst = Solution()
print(inst.convert(s, n))