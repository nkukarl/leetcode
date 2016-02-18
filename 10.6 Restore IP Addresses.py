class Solution:
	def restoreIpAddresses(self, s):
		self.res = []
		self.helper(s, [])

		return self.res

	def helper(self, s, cur):
		if not s:
			if len(cur) == 4:
				self.res.append('.'.join(cur))
		else:
			self.helper(s[1:], cur + [s[0]])
			if len(s) >= 2:
				if len(str(int(s[:2]))) == 2:
					self.helper(s[2:], cur + [s[:2]])
			if len(s) >= 3:
				if len(str(int(s[:3]))) == 3 and int(s[:3]) <= 255:
					self.helper(s[3:], cur + [s[:3]])

s = '25525511135'
s = '0101011'

inst = Solution()
print(inst.restoreIpAddresses(s))