class Solution:
	def intToRoman(self, n):
		RR = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
		II = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		s = ''
		for i in range(len(II)):
			s += (n // II[i]) * RR[i]
			n %= II[i]
		return s

n = 1120

inst = Solution()
print(inst.intToRoman(n))
