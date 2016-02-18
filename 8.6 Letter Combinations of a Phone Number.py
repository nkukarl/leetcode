MAP = {'0': ' ', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

class Solution:
	def letterCombinations(self, s):
		self.res = []

		self.helper(s, '')

		return self.res

	def helper(self, s, cur):
		if not s:
			self.res.append(cur)
		else:
			for char in MAP[s[0]]:
				self.helper(s[1:], cur + char)

s = '234'

inst = Solution()
print(inst.letterCombinations(s))

