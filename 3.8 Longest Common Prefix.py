class Solution:
	def longestCommonPrefix(self, strs):
		prefix = ''
		s0 = strs[0]
		for i in range(len(s0)):
			for s in strs[1:]:
				if i >= len(s) or s[i] != s0[i]:
					return prefix
			prefix += s0[i]
		return prefix

strs = ['abd', 'abd', 'abcd']

inst = Solution()
print(inst.longestCommonPrefix(strs))
